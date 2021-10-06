from django.shortcuts import render

def tudenovi(request):
    return render(request, 'tudenovi.html', {})
