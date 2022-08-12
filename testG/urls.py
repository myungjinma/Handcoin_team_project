from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    path("play/", views.play),
]
