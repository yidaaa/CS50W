from django.urls import path
from . import views

# from views.py, see index
urlpatterns = [
    path("", views.index, name="index"),
    path("brian", views.brian, name="brian"),
    path("<str:name>", views.greet, name="greet"),
]