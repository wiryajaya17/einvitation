from django.contrib import admin
from django.urls import path, include
import weddingpage.views

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('',include('weddingpage.urls')),
    path('test/', weddingpage.views.test, name='test'),
    path('', weddingpage.views.home, name='home'),
    path('blissful/',include('weddingpage.urls')),
    path('twainlove/',include('twainlove.urls')),
]
