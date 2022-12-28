
from django.contrib import admin
from django.urls import path

from familia.views import crear_familiar, lista_familia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear_familiar/', crear_familiar),
    path('familia/', lista_familia)
]
