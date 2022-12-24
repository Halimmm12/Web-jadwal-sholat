from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Kategori)

# class ArtikelAdmin(admin.ModelAdmin):
#     list_display = ('nama','jadwal','date','kategori')
# admin.site.register(Artikel, ArtikelAdmin)

class JadwalSholatAdmin(admin.ModelAdmin):
    list_display = ('nama','jadwal','kategori','waktu','tanggal')
admin.site.register(JadwalSholat, JadwalSholatAdmin)

class JadwalAdmin(admin.ModelAdmin):
    list_display = ['tanggal','imsyak','shubuh','terbit','dhuha','dzuhur','ashr','magrib','isya']
    
admin.site.register(ApiJadwal, JadwalAdmin)

class DoaAdmin(admin.ModelAdmin):
    list_display = ['id','doa','ayat','latin','artinya']
    
admin.site.register(DoaIslami, DoaAdmin)




