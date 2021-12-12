from django.shortcuts import render

def metatah(request, message = ''):
    query = message
    context = {
        'message' : query,
    }
    return render(request, 'metatah.html', context)
