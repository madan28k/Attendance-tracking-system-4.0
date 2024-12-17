from django.urls import path
from . import views

urlpatterns = [
    path("", views.faculty_view, name="faculty_view"),
    path("add_manually", views.add_manually, name="add_manually"),
    path("generate_excel/", views.generate_excel, name="generate_excel"),
]
