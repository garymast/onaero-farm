from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("", views.about_us, name="about_us"),
]
