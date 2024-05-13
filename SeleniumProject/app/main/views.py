from django.shortcuts import render
from django.http import JsonResponse
from .models import Tenders, Keywords
from .tender_data import update_data

def prikazi_tendere(request):
    tenders = Tenders.objects.all()
    # update_data()
    return render(request, 'index.html', {'tenders': tenders})

def update_keywords(request):
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        Keywords.objects.create(kljucne_rijeci=keywords)
        return JsonResponse({'message': 'Rijeci su uspjesno dodate!'})
    return render(request, 'index.html')

# def pretraga_i_spremanje_tendera(request):
#     update_data()
#     return JsonResponse({'message': 'Tenderi su uspješno pretraženi i dodani u bazu!'})

