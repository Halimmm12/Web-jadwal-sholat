from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import JadwalSholat, ApiJadwal, DoaIslami

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.db import  transaction
from django.contrib.auth.hashers import make_password
from users.models import Biodata
import requests
     
# API JADWAL SHOLAT
def sinkron_jadwal(request):
	url = "https://raw.githubusercontent.com/lakuapik/jadwalsholatorg/master/adzan/samarinda/2022/12.json"
	data = requests.get(url).json()
	for d in data:
		cek_berita = ApiJadwal.objects.filter(tanggal=d['tanggal'])
		if cek_berita:
			print('data sudah ada')
			c = cek_berita.first()
			c.tanggal=d['tanggal']
			c.save()
		else: 
      		#jika belum ada maka tulis baru kedatabase
			b = ApiJadwal.objects.create(
				tanggal = d['tanggal'],
				imsyak = d['imsyak'],
				shubuh = d['shubuh'],
				terbit = d['terbit'],
				dhuha = d['dhuha'],
				dzuhur = d['dzuhur'],
				ashr = d['ashr'],
				magrib = d['magrib'],
				isya = d['isya'],
			)
	return redirect(home)

# API DOA 
def doa_muslim(request):
    url = "https://doa-doa-api-ahmadramadhan.fly.dev/api"
    data =  requests.get(url).json()
    for z in data :
        cek_doa = DoaIslami.objects.filter(id=z['id'])
        if cek_doa :
            print('data sudah ada')
            a = cek_doa.first()
            a.id = z['id']
            a.save()
        else : 
            f = DoaIslami.objects.create(
                id = z['id'],
                doa = z['doa'],
                ayat = z['ayat'],
                latin = z['latin'],
                artinya = z['artinya'],
                )
                
    return redirect(home)
        
def home(request):
    template_name = 'front/home.html'
    jadwal_sholat = JadwalSholat.objects.all()
    api_jadwal = ApiJadwal.objects.all()
    context = {
        'title':'my home',
        'jadwal_sholat':jadwal_sholat,
        'api_jadwal': api_jadwal
    }
    return render(request, template_name, context)

def base(request):
    template_name = 'front/base.html'
    context = {
        'title':'Tabel',
    }
    return render(request, template_name, context)

def blog(request):
    template_name = 'front/blog.html'
    context = {
        'title':'form',
    }
    return render(request, template_name, context)

def script(request):
    template_name = 'front/script.js'
    context = {
        'title':'js',
    }
    return render(request, template_name, context)

def doaislami(request):
    template_name = 'front/doaislami.html'
    doa_islami = DoaIslami.objects.all()
    context = {
        'title':'doaislami',
        'doa_islami': doa_islami
    }
    return render(request, template_name, context)

# def login(request):
#     template_name = 'account/login.html'
#     if request.method == "POST":
#         print('POST')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username, password)
#     context = {
#         'title':'form-login',
#     }
#     return render(request, template_name, context)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    template_name = 'account/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            pass
            print("username dan password benar" )
            auth_login(request, user)
            return redirect('home')
        else:
            pass
            print("username dan password anda salah" )
    context = {
        'title':'form',
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect ('login')


def registrasi(request):
    template_name = "account/register.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')
        telp = request.POST.get('telp')
        try:
            with transaction.atomic():
                User.objects.create(
                    username = username,
                    password  = make_password(password),
                    first_name = nama_depan,
                    last_name = nama_belakang,
                    email = email   
                )
                get_user = User.objects.get(username = username)
                Biodata.objects.create(
                    user = get_user,
                    alamat = alamat,
                    telp = telp,
                )
            return redirect(home)
        except : pass

    context = {
        'title':'register'      
    }
    
    return render(request, template_name, context)
    



