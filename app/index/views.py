from django.shortcuts import render
from ..bot.models import MetasCompleted


def index(request):
    result = MetasCompleted.objects.all()
    for r in result:
        print()
    return render(request, "index/index.html", {"result": result})


