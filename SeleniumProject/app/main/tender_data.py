from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import schedule
import time
from .models import Tenders


def update_data():
    dan, mesec, godina = datetime.now().day, datetime.now().month, datetime.now().year
    formatirani_datum = f"{dan}.{mesec}.{godina}"
    print(formatirani_datum)

    driver = webdriver.Chrome()
    driver.get("https://cejn.gov.me/tenders")

    try:
        message_window = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "cdk-overlay-0"))
        )

        WebDriverWait(driver, 10).until_not(
            EC.visibility_of_element_located((By.CLASS_NAME, "loading-shade"))
        )


        ok_button = message_window.find_element(By.XPATH, ".//button[contains(@class, 'doneBtn')]")
        ok_button.click()
        print("")

    except Exception as e:
        print("Prozor nije pronadjen ili se pojavila greska:", e)

    opisi_tendera = driver.find_elements(By.CLASS_NAME, "colTitle")

    for opis_tendera in opisi_tendera:
        tekst_opisa = opis_tendera.text
        keywords = ['marketing', 'materijal', 'digital', 'brosura', 'flajer', 'dizajn', 'websajt', 'veb sajt',
                    'aplikacija', 'aplikacije', 'facebook', 'google', 'seo', 'hosting', 'media buying', 'reklamiranje',
                    'reklama', 'reklame', 'advertising', 'kreativa']

        # Roditeljski <tr> element koji sadrzi trenutni opis tendera
        parent = opis_tendera.find_element(By.XPATH, "./ancestor::tr")

        status = parent.find_element(By.CLASS_NAME, "colStatus").text
        datum_objave = parent.find_element(By.CLASS_NAME, "colPublishedOn").text

        datum_objave = datum_objave.split()[0]

        if status.strip() == "U toku" and any(kljucna_rijec in tekst_opisa.lower() for kljucna_rijec in keywords):
            if datum_objave.strip() == formatirani_datum:
                sifra = parent.find_element(By.CLASS_NAME, "colId").text

                print("Opis tendera:", tekst_opisa)
                print("Status:", status)
                print("Datum objave:", datum_objave)
                print("Šifra tendera:", sifra)
                print("-" * 30)

                # tender = Tenders.objects.get_or_create(
                #     opis=tekst_opisa,
                #     status=status,
                #     datum_objave=datum_objave,
                #     sifra=sifra
                # )

    driver.quit()


# Azuriranja podataka svakog dana u 23:59h
schedule.every().day.at("13:33").do(update_data)

while True:
    schedule.run_pending()
    time.sleep(1)