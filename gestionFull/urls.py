from django.urls import path
from . import views

app_name = 'autenticacion'
urlpatterns = [
   path('registrarse/', views.signup, name='registrarse'),
   path('logueo/', views.custom_login, name='logueo')
]