from django.db.models import Count
from django.shortcuts import render
from django.utils.timezone import utc
#from django.views.generic import TemplateView
from .models import worklist
from versioncheck.models import versioncheckv
import datetime
# Create your views here.


def index(request):
    # template_name = "home.html" (bu satır template view classı kullanıldığında belirtilmesi gerekir)
    #workall = worklist.objects.all() #bu kısım veritabanındaki bütün bilgileri göstermek içindir kullanmak için yorum satırını kaldırınız
    merged = worklist.objects.filter(durum__contains='Merge Edilecek')
    devoloping = worklist.objects.filter(durum__contains='Geliştiriliyor')
    review = worklist.objects.filter(durum__contains='Review')
    testfinish = worklist.objects.filter(durum__contains='Testten Döndü')
    teststart = worklist.objects.filter(durum__contains='Test Edilecek')
    emergency = worklist.objects.filter(öncelik__contains='Acil')
    #state = worklist.objects.values("durum").annotate(count=Count('ticketid')) #bu kısım veritabanındaki durum kolonu altındaki ticketid sayıları içindir kullanmak için yorum satırını kaldırınız
    mergedsayisi = worklist.objects.filter(durum__contains='Merge Edilecek').count()
    devolopingsayisi = worklist.objects.filter(durum__contains='Geliştiriliyor').count()
    reviewsayisi = worklist.objects.filter(durum__contains='Review').count()
    testfinishsayisi = worklist.objects.filter(durum__contains='Testten Döndü').count()
    teststartsayisi = worklist.objects.filter(durum__contains='Test Edilecek').count()
    emergencysayisi = worklist.objects.filter(öncelik__contains='Acil').count()

    versiyon = versioncheckv.objects.filter(type='versiyon').first()
    staging = versioncheckv.objects.filter(type='staging').first()
    versiyon_tarihi = ''
    versiyon_kalan_sure = ''
    versiyon_adi = ''
    staging_tarihi = ''
    if versiyon:

        versiyon_zamani = versiyon.exportdate
        now = datetime.datetime.now(utc)
        versiyon_kalan_sure = (versiyon_zamani - now).days
        versiyon_tarihi = datetime.datetime.strftime(versiyon.exportdate, '%d/%m/%Y')
        versiyon_adi = versiyon.versionname
    if staging:
        staging_tarihi = datetime.datetime.strftime(staging.exportdate, '%d/%m/%Y')

    extra_context = {
        'merged': merged,
        #'workall': workall, #bu kısım veritabanındaki bütün bilgileri göstermek içindir. Kullanmak için yorum satırını kaldırınız
        'devoloping': devoloping,
        'review': review,
        'testfinish': testfinish,
        'teststart': teststart,
        'emergency': emergency,
        'mergedsayisi': mergedsayisi,
        'devolopingsayisi': devolopingsayisi,
        'reviewsayisi' : reviewsayisi,
        'testfinishsayisi' : testfinishsayisi,
        'teststartsayisi' : teststartsayisi,
        'emergencysayisi' : emergencysayisi,
        'staging': staging,
        'calisilan_versiyon': versiyon,
        'versiyon_tarihi': versiyon_tarihi,
        'versiyon_kalan_sure': versiyon_kalan_sure,
        'versiyon_adi': versiyon_adi,
        'staging_tarihi': staging_tarihi,
    }
    return render(request, 'home.html', context=extra_context)


