from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.relay_list, name='relay_list'),
    
    
]