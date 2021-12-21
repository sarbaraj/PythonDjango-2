#1. import
from django.http import HttpResponse

#2. create function
def index(request):
    return HttpResponse("Hello world of Django!")