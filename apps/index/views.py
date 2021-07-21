from django.shortcuts import render
from ..bot.models import DoneList, Profile


def index(request):
    #user = Profile.objects.all()
    result = DoneList.objects.all()
    
    return render(request, "index/index.html", {"result": result})


