from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="index"),
    path("home",home,name="home"),
    path("about",about,name="about"),
    path("contact",contact,name="contact"),
]