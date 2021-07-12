from django.shortcuts import render
from ..bot.models import MetasCompleted, Profile


def index(request):
    #user = Profile.objects.all()
    result = MetasCompleted.objects.all()
    
    return render(request, "index/index.html",{"result": result})


