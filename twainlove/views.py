from django.shortcuts import render

def twainlove(request):
    return render(request, 'twainlove.html', {})
