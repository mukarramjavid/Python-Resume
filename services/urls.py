from django.urls import path
from . import views as s
urlpatterns = [
    
    path('my-services/',s.Services,name='services'),
]