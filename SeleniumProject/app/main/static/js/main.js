document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(form);
        fetch(form.action, {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1);
    var yyyy = today.getFullYear();
    today = dd + '.' + mm + '.' + yyyy;
    console.log(today)

    document.getElementById('today_date').textContent = today;

    var tenders = document.querySelectorAll('.tender');

    tenders.forEach(function (tender) {
        var status = tender.querySelector('.status').textContent;
        var datumObjave = tender.querySelector('.datum_objave').textContent;

        if (datumObjave === today && status === 'U toku') {
        } else {
            tender.parentElement.style.display = 'none';
        }
    });
});

function pogledajTender(tenderSifra) {
    var url = "https://cejn.gov.me/tenders/view-tender/" + tenderSifra;

    window.open(url, '_blank');
}