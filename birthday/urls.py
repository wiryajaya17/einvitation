from django.urls import path
from . import views

urlpatterns = [
    path('', views.raveena, name="raveena"),
    path('wishes', views.wishes, name="wishes"),
]
