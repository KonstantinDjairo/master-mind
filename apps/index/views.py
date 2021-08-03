from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from ..bot.models import DoneList, Profile


def index(request):
    result = DoneList.objects.all()
    
    return render(request, "index/index.html", {"result": result})


def player_detail(request, id_user):
    player = get_object_or_404(Profile, id_user=id_user)
    # terminar
