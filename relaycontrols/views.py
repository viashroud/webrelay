from django.shortcuts import render
from .models import Relay

def relay_list(request):
    relays = Relay.objects.all()
    return render(request, 'relaycontrols/relay_list.html', {'relays': relays})
