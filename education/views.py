from django.shortcuts import render

# Create your views here.
def Skills(request):
    context={'skill':'active'}
    return render(request,'skills/skill.html',context)