from django.urls import path
from . import views as skill
urlpatterns = [
    
    path('my-skills/',skill.Skills,name='skills'),
]