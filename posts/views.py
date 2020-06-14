"""Application views"""

from django.http import HttpResponse
from posts.models import User

def list_posts (request):
    """List existing posts"""
    return HttpResponse('Hello from new app')


"""Example script for managing Django ORM's"""

# def orm_wrapper(request):
#     """Playing with django's ORM"""

#     # Desde acá ya creó el objeto en base de datos
#     pablo = User.objects.create( 
#         email='hola@gmail.com', 
#         password='1234567', 
#         first_name='pablo',
#         last_name='trinidad' 
#     )

#     pablo.email = 'otro_email@email.com'
#     pablo.save()

#     # Segunda manera: Instanciamos el objeto, pero no lo guardamos hasta que se indique la operación save()
#     ignacio = User(
#         email='gsikmo@gmail.com',
#         password='1234567',
#         first_name='Ignacio',
#         last_name='Martinez'
#     )

#     # Aquí ya existirá en la BD
#     ignacio.save()

#     # Así borramos un usuario
#     pablo.delete()

#     ## Otro script. Obtiene un objeto directo de la base de datos
#     ignacio2 = User.objects.get(email='gsikmo@gmail.com')

#     type(ignacio2)

#     all = User.objects.filter(email__endswith='.com')

#     affected = User.objects.filter(email__endswith='.com').update(bio='nada para mostrar')