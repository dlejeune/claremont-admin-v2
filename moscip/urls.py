from django.urls import path

from . import views
from . import scout_views

urlpatterns = [
    path("scouts/", scout_views.view_all_scouts, name="view_all_scouts"),
    path("", views.index, name="index"),

]
