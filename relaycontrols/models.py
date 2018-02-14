from django.db import models
from django.utils import timezone

class Relay(models.Model):
    pin_number = models.IntegerField()
    name = models.CharField(max_length=200)
    current_state = models.BooleanField()
    
    def create_relay(self):
        self.save()
        
    def __str__ (self):
        return self.name
    
