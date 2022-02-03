from django.shortcuts import render
from twainlove.models import Rsvp
from datetime import datetime

def raveena(request, message = ''):
    # rsvps = Rsvp.objects.filter(name='Wirwir')
    # rsvps = Rsvp.objects.post_date__gte=datetime.date.today()
    query = message
    rsvps = Rsvp.objects.filter(owner='raveena').order_by('-post_date')
    return render(request, 'raveena.html', {'rsvps' : rsvps, 'message' : query})

def wishes(request):
    if request.method == 'POST':
        rsvp = Rsvp()
        rsvp.owner = 'raveena'
        rsvp.name = request.POST['name']
        rsvp.email = ''
        rsvp.num_of_rsvp = 1
        rsvp.flag_attending = 'Y'
        rsvp.message_body = request.POST['message_body']
        rsvp.save()
        return render(request,'wishes.html', {})
    else:
        return render(request, 'raveena.html', {})
    # return render(request,'create.html', {})
