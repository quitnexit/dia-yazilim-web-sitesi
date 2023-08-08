from django.db import models
from datetime import datetime

class versioncheckv(models.Model):
    versionname = models.CharField(max_length=20)
    exportdate =models.DateTimeField()
    type = models.CharField(max_length=32)
    importdate = models.DateTimeField(default=datetime.now())