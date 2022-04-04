from django.shortcuts import render
from datetime import datetime

def homepage(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def featuresType(request):
    return render(request, 'features-type.html')
