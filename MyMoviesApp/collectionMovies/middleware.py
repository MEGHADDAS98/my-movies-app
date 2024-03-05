from .models import RequestCounter

class RequestCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.counter = RequestCounter.objects.get_or_create(counter=0)[0]
        response.counter.increment()
        return response

def middleware(get_response):
    def middleware_view(request):
        response = get_response(request)
        response.counter = RequestCounter.objects.get_or_create(counter=0)[0]
        response.counter.increment()
        return response
    return middleware_view