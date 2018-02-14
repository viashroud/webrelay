from django.shortcuts import render
from .models import Relay

def base(request):
    relays = Relay.objects.all()
    return render(request, 'relaycontrols/base.html', {'relays': relays})
