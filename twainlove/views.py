from django.shortcuts import render
from .models import Rsvp

def twainlove(request):
    rsvps = Rsvp.objects
    return render(request, 'twainlove.html', {'rsvps' : rsvps})

def create(request):
    if request.method == 'POST':
        rsvp = Rsvp()
        rsvp.name = request.POST['name']
        rsvp.email = request.POST['email']
        rsvp.num_of_rsvp = request.POST['num_of_rsvp']
        rsvp.flag_attending = request.POST['flag_attending']
        rsvp.message_body = request.POST['message_body']
        rsvp.save()
        return render(request,'create.html', {})
    else:
        return render(request, 'twainlove.html', {})
    # return render(request,'create.html', {})
