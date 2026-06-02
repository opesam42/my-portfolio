from django.shortcuts import reverse, redirect
from django.conf import settings
from django.db import connections
from django.db.utils import OperationalError
from django.core.cache import cache

class MaintenanceModeMiddleware:

    """ Set this up purposely because of AIVEN Database Maintenance, so users won't see a 500 Server Error """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.META.get('PATH_INFO', "")
        
        # Skip check for maintenance page itself
        if path == reverse("core:maintenance"):
            return self.get_response(request)
        
        # Check database connectivity
        db_available = self._check_database()

        if not db_available:
            return redirect(reverse("core:maintenance"))
            
        return self.get_response(request)
    
    def _check_database(self):
        db_status = cache.get("db_health")

        if db_status is not None:
            return db_status
        
        # Cache Miss
        try:
            connections['default'].ensure_connection()
            cache.set("db_health", True, timeout=30) # timeout 30 seconds
            return True
        except OperationalError:
            cache.set("db_health", False, timeout=10) # timeoout = 10s if the db is not available 
            return False