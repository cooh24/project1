from django.db import models

# Create your models here.
class WildFireData(models.Model):
    ocudt_y = models.CharField(max_length=4)
    ocudt_d = models.CharField(max_length=2)
    ocudt_m = models.CharField(max_length=2)
    ocurdo = models.CharField(max_length=2)
    ocursgg = models.CharField(max_length=8)
    exintgtm = models.IntegerField
    ocurcause = models.TextField
    dmgarea = models.FloatField
    dmgmoney = models.FloatField
    tempavg = models.FloatField
    humidcurr = models.FloatField
    humidrel = models.FloatField
    windavg = models.FloatField
    diravg = models.CharField(max_length=4)

    class Meta:
        verbose_name_plural = "산불발생 데이터"