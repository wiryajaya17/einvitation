from django.shortcuts import render

def metatah(request):
    return render(request, 'metatah.html', {})
