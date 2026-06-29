import threading
from django.core.mail import send_mail
from django.conf import settings

def send_downtime_alert():
    thread = threading.Thread(
        target=lambda: send_mail(
            subject='Portfolio DB Down',
            message='Your database is unreachable. Maintenance page is now active.',
            from_email=settings.DEFAULT_FROM_EMAIL,  # who sends it
            recipient_list=[settings.ADMIN_EMAIL],   # who receives it
            fail_silently=False
        )
    )
    thread.daemon = True  # daemon=True so the email never blocks the HTTP response -> so the page shows in milliseconds and the email sending runs separately 
    thread.start()