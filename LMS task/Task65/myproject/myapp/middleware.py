import time
from django.http import HttpResponseForbidden

class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()
        print(f"Request to {request.path} took {end_time - start_time:.4f} seconds")
        return response


class BlockIPMiddleware:
    BLOCKED_IPS = ["127.0.0.2"]  # example IP

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        if ip in self.BLOCKED_IPS:
            return HttpResponseForbidden("Access blocked")
        return self.get_response(request)
