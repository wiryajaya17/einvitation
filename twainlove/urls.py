from django.urls import path
from . import views

urlpatterns = [
    path('', views.twainlove, name="twainlove"),
]
