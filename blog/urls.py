from django.urls import path ,include
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('JadwalLim/',JadwalLim, name='tabel_artikel'),
    path('Jadwal/tambah',tambah_jadwal, name='tambah_jadwal'),
    path('Jadwal/lihat/<str:id>',lihat_jadwal, name='lihat_jadwal'),
    path('Jadwal/edit/<str:id>',edit_jadwal, name='edit_jadwal'),
    path('artikel/hapus/<str:id>',hapus_jadwal, name='hapus_jadwal'),
    path('users/',users, name='tabel_users'),
]


