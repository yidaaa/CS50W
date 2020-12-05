from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.newpage, name="newpage"),
    path("random", views.random_entry, name="random"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("<str:title>", views.entry, name="entry"),
]
