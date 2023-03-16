from django.urls import path
from app3.views import *
app_name="app3"
urlpatterns=[
    
    path('dilli/',dilli,name='dilli')
]