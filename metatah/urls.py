from django.urls import path
from . import views

urlpatterns = [
    path('', views.metatah, name="metatah"),
]
