from django.db import models
from django.contrib import admin

class Prescriptions(models.Model):

    file_url=models.URLField(max_length=256)
    od_power_sph=models.CharField(max_length=60, null=True, blank=True)
    od_bc=models.CharField(max_length=56, null=True, blank=True)
    od_dia=models.CharField(max_length=56, null=True, blank=True)
    od_cyl=models.CharField(max_length=56, null=True, blank=True)
    od_axis=models.CharField(max_length=56, null=True, blank=True)
    os_power_sph=models.CharField(max_length=56, null=True, blank=True)
    os_bc=models.CharField(max_length=56, null=True, blank=True)
    os_dia=models.CharField(max_length=56, null=True, blank=True)
    os_cyl=models.CharField(max_length=56, null=True, blank=True)
    os_axis=models.CharField(max_length=56, null=True, blank=True)

    def __str__(self):
        return self.file_url

admin.site.register(Prescriptions)