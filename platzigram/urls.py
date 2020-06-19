"""Application URL's."""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# views
from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [

    path('hola/', local_views.hola_mundo),
    path('analisis-response/', local_views.analizando_HttpResponse),
    path('myname/<str:myName>', local_views.nameHandler),
    path('posts/', posts_views.list_posts, name='feed'),
    path('admin/', admin.site.urls, name='admin'),
    path('users/login', users_views.login_view, name='login'),
    path('users/logout', users_views.logout_view, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
