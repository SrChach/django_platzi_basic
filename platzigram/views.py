"""Project views."""

# Django
from django.http import HttpResponse

def hola_mundo (request):
    """Return a greeting"""
    return HttpResponse('Hello World!')

def analizando_HttpResponse (request):
    """Debug en consola de un request, usando list-comprehension"""
    import pdb; pdb.set_trace()
    return HttpResponse('Analiza el objeto "request" de tipo "HttpResponse" en la consola!')

def nameHandler (request, myName):
    return HttpResponse('Welcome {}!'.format(myName))
