from django.db import models

class Tenders(models.Model):
    opis = models.TextField()
    status = models.TextField()
    datum_objave = models.TextField()
    sifra = models.TextField()

    def __str__(self):
        return f"Opis tendera: {self.opis} | Status tendera: {self.status} | Sifra tendera: {self.sifra}"

class Keywords(models.Model):
    kljucne_rijeci = models.TextField()

    def __str__(self):
        return "Kljucne rijeci"
