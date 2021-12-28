from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app4/index.html')

def contact(request):
    return render(request, 'app4/Contacts.html')

def cookbook(request):
    return render(request, 'app4/CookBook.html')

def cuisine(request):
    return render(request, 'app4/Cuisine.html')

def wine(request):
    return render(request, 'app4/Wine.html')

