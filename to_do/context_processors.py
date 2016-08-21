from django.conf import settings

def static_url(request):
    return {
        'STATIC_URL': settings.STATIC_URL
    }

def media_url(request):
    return {
        'MEDIA_URL': settings.MEDIA_URL
    }
