from django.contrib import admin
from django.urls import path
from platzigram.views import (hola_mundo, analizando_HttpResponse, nameHandler)

urlpatterns = [
    path('hola/', hola_mundo),
    path('analisis-response/', analizando_HttpResponse),
    path('myname/<str:myName>', nameHandler),
    path('admin/', admin.site.urls)
]