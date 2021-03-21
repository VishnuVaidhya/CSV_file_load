from django.db import models

# Create your models here.

#class Date_Store(models.Model):
#    date = models.DateField(auto_now_add=False)

class Date_store(models.Model):
    rate = models.IntegerField()
    symbole = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=False)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()
    adjclose = models.FloatField()