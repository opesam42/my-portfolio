from django.conf import settings

def branding(request):
    return {
        'MY_NAME': settings.MY_NAME,
        'MY_TAGLINE': settings.MY_TAGLINE,
        'WHATSAPP_LINK': settings.WHATSAPP_LINK,
        'EMAIL_ADDRESS': settings.EMAIL_ADDRESS,
        'GITHUB_URL': settings.GITHUB_URL,
        'LINKEDIN_URL': settings.LINKEDIN_URL,
        'DEV_TO_URL': settings.DEV_TO_URL,
        'X_URL': settings.X_URL,
        'MEDIUM_URL': settings.MEDIUM_URL
    }