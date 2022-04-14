# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# Unable to inspect table 'table'
# The error was: (1146, "Table 'wildfireDB.table' doesn't exist")


class Wildfire(models.Model):
    ocurdt_y = models.CharField(max_length=4, blank=True, null=True)
    ocurdt_m = models.CharField(max_length=2, blank=True, null=True)
    ocurdt_d = models.CharField(max_length=2, blank=True, null=True)
    ocurdo = models.CharField(max_length=2, blank=True, null=True)
    ocursgg = models.CharField(max_length=8, blank=True, null=True)
    exintgtm = models.IntegerField(blank=True, null=True)
    ocurcause = models.TextField(blank=True, null=True)
    dmgarea = models.FloatField(blank=True, null=True)
    dmgmoney = models.FloatField(blank=True, null=True)
    tempavg = models.FloatField(blank=True, null=True)
    humidcurr = models.FloatField(blank=True, null=True)
    humidrel = models.FloatField(blank=True, null=True)
    windavg = models.FloatField(blank=True, null=True)
    diravg = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        db_table = 'wildfire'

    def __str__(self):
        return f'{self.ocurdt_y}{self.ocurdt_m}{self.ocurdt_d}--{self.ocurdo}{self.dmgarea}'