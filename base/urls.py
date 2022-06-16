from django.urls import path
from . import views

urlpatterns = [
    path('', views.basehome, name='basehome'),
]