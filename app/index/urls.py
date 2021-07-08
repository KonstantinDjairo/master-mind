from django.urls import path
from app.index.views import index

urlpatterns = [
    path('', index, name='index'),
]