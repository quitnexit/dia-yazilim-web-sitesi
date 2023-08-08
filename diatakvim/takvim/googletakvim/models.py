from django.db import models
class worklist(models.Model):
    ticketid = models.IntegerField(primary_key=True)
    iş_tipi = models.TextField()
    durum = models.TextField()
    öncelik = models.TextField()
    atanan = models.TextField()
    hedef_sürüm = models.TextField()
    kalan_zaman = models.TextField()

