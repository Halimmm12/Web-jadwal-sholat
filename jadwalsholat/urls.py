from django.contrib import admin
from django.urls import path ,include
from blog.views import *

from . views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404,handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('blog.urls')),

    path('', home, name='home'),
    path('base', base, name='base'),
    path('blog', blog, name='blog'),
    path('script', script, name='script'),
    path('doaislami', doaislami, name='doaislami'),
    path('sinkron_jadwal', sinkron_jadwal, name='sinkron_jadwal'),
    path('doa_muslim', doa_muslim, name='doa_muslim'),
    
    #login dan logout
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registrasi, name='registrasi'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

