from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from ..bot.models import DoneList, Profile


def index(request):

    object_list = Profile.objects.all()
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        profiles = paginator.page(1)
    except EmptyPage:
        profiles = paginator.page(paginator.num_pages)

    return render(request, "index/index.html", {'page': page, 'profiles': profiles})



