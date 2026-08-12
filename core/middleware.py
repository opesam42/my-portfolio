from django.shortcuts import reverse, redirect
from django.db import connections
from django.db.utils import OperationalError
from django.core.cache import cache
from .services import send_downtime_alert

class MaintenanceModeMiddleware:

    """ Set this up purposely because of AIVEN Database Maintenance, so users won't see a 500 Server Error """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.META.get('PATH_INFO', "")
        maintenance_path = reverse("core:maintenance")

        # Check database connectivity
        db_available = self._check_database()

        # when a user try to access maintenance page directly, they get routed to the homepage
        if path == maintenance_path:
            if db_available:
                return redirect(reverse("core:home"))
            return self.get_response(request)

        if not db_available:
            return redirect(reverse("core:maintenance"))

        try:
            return self.get_response(request)
        except OperationalError:
            # DB dropped mid-request (e.g. SSL connection closed during rendering)
            return redirect(maintenance_path)
    
    def _check_database(self):
        db_status = cache.get("db_health")

        if db_status is not None:
            return db_status
        

        # Cache Miss — use a real query, not just ensure_connection(), to catch dropped SSL connections
        try:
            conn = connections['default']
            conn.ensure_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")
            cache.set("db_health", True, timeout=30)
            return True
        except OperationalError:
            cache.set("db_health", False, timeout=10) # timeoout = 10s if the db is not available 

            # send alert 
            alert_already_sent = cache.get("db_downtime_alert_sent")
            if not alert_already_sent:
                send_downtime_alert()
                cache.set("db_downtime_alert_sent", True, timeout=1800) # 30 mins

            return False