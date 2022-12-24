from django.shortcuts import render, redirect
from multiprocessing import context
# 7:35
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Kategori, JadwalSholat

# 34:40
def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else :    
        return False

# 7:35
@login_required
def dashboard(request):     
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'  
    template_name = "back/dashboard.html"
    context = {
        'title' : 'dashboard',
    }
    return render(request, template_name, context)
 
# baru
@login_required
def JadwalLim (request):
    template_name = "back/tabel_artikel.html"
    JadwalLim = JadwalSholat.objects.all()
    context = {
        'title': 'JadwalLim',
        'JadwalLim' : JadwalLim,
    }
    
    return render(request, template_name, context)

@login_required
def tambah_jadwal(request):
    template_name = "back/tambah_artikel.html"
    kategori = Kategori.objects.all()
    print(kategori)
    if request.method == "POST":
        nama = request.POST.get('nama')
        jadwal = request.POST.get('jadwal')
        kategori = request.POST.get('kategori')
        waktu = request.POST.get('waktu')
        tanggal = request.POST.get('tanggal')
        
        # memanggil kategori
        kat = Kategori.objects.get(nama=kategori)
        
        
        JadwalSholat.objects.create(
            nama = nama,
            jadwal = jadwal,
            kategori = kat,
            waktu = waktu,
            tanggal = tanggal,
        ) 
        return redirect(JadwalLim)
    
    context = {
        'title' : 'Tambah Data',
        'kategori' : kategori,
    }   
    return render(request, template_name, context)

@login_required
def lihat_jadwal(request, id):
    template_name = "back/lihat_artikel.html"
    jadwalsholat = JadwalSholat.objects.get(id=id)
    context = {
        'title' : 'Lihat Informasi Jadwal',
        'jadwalsholat' : jadwalsholat,
    }
    return render(request, template_name, context)

@login_required
def users(request):
    template_name = "back/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title' : 'INPUT USER',
        'list_user' : list_user
    }  
    return render(request, template_name, context)

# edit artikel
@login_required
def edit_jadwal(request, id):
    template_name = "back/edit_artikel.html"
    a = JadwalSholat.objects.get(id=id)
    if request.method == "POST":
        nama = request.POST.get('nama')
        jadwal = request.POST.get("jadwal")
        
        print(nama, jadwal)
        # save data
        a.nama = nama
        a.jadwal = jadwal

        a.save()
        return redirect(JadwalLim)
    
    
    context = {
        'title' : 'Edit Informasi',
        'JadwalLim': a,
        
    }
    return render(request, template_name, context)

    def AdminJadwal(request):
        template_name = "back/tabel_users.html"
        list_user = User.objects.all()
        context = {
        'title' : 'INPUT USER',
        'list_user' : list_user
    }  
    return render(request, template_name, context)

# edit artikel
@login_required
def hapus_jadwal(request, id):
    JadwalSholat.objects.get(id=id).delete()
    return redirect(JadwalLim)


