# Django
from django.contrib import admin
from django.urls import path

# views
from platzigram import views as local_views
from posts import views as external_views

urlpatterns = [
    path('hola/', local_views.hola_mundo),
    path('analisis-response/', local_views.analizando_HttpResponse),
    path('myname/<str:myName>', local_views.nameHandler),
    path('external/', external_views.list_posts),
    path('admin/', admin.site.urls)
]
