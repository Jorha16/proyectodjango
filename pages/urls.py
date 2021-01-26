from django.urls import path
from . import views

urlpatterns = [
    path('pagina/<str:slug>',views.Page, name="page"),
]