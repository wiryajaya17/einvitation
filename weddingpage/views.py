from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def blissful(request):
    return render(request, 'blissful.html', {})

def test(request):
    return render(request, 'testpage.html', {})
