from django.urls import path
from PlayApp import views

urlpatterns = [
    path('', views.inicio,name = "Inicio"),
    # path('view/', views.primer_view,),
    path('usuario/', views.usuario, name = "Usuario"),
    path('publicaciones/', views.publicaciones, name = "Publicaciones"),
    path('about/', views.sobre_nosotros, name = "Sobre Nosotros"),
]
