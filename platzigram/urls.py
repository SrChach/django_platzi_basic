from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def hola_mundo (request):
    return HttpResponse('Hello World!')

urlpatterns = [
    path('hola/', hola_mundo),
    path('admin/', admin.site.urls)
]