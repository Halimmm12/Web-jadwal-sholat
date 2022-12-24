from django.db import models

# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "Kategori"


class JadwalSholat(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    jadwal = models.CharField(max_length=100, blank=True, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True, null=True )
    waktu = models.CharField(max_length=30, blank=True, null=True)
    tanggal = models.DateField(True, blank=True, null=True)
      
    def __str__(self):
        return "{} - {}".format(self.nama, self.nama)
    
    class Meta:
        ordering = ['-tanggal']
        verbose_name_plural = "JadwalSholat"
        
# API
        
class ApiJadwal(models.Model):
    tanggal = models.DateField(max_length=255, unique=True)
    imsyak = models.TimeField()
    shubuh = models.TimeField()
    terbit = models.TimeField()
    dhuha = models.TimeField()
    dzuhur = models.TimeField()
    ashr = models.TimeField()
    magrib = models.TimeField()
    isya = models.TimeField()
    
    def _str_(self):
        return self.tanggal
    
class DoaIslami(models.Model):
    id = models.IntegerField(primary_key=True)
    doa = models.TextField()
    ayat = models.TextField()
    latin = models.TextField()
    artinya = models.TextField()
    
    def _str_(self):
        return self.tanggal
    
    
        
    