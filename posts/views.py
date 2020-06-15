"""Application views"""

from django.http import HttpResponse

def list_posts (request):
    """List existing posts"""
    return HttpResponse('Hello from new app')
