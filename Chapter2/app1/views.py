from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'app1\\index.html')

def about(request):
    return render(request, 'app1\\about.html')

def products(request):
    return render(request, 'app1\\products.html')

def gallery(request):
    return render(request, 'app1\\gallery.html')
