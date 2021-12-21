from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # read value from request
    return HttpResponse("Hello from app3")