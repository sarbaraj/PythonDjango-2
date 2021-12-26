from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    # Model
    # return HttpResponse(str(result))
    return render(request, 'app3/index.html')

def new(request):
    return render(request, 'app3/new.html')

def receivenew(request):
    # Recive value(s) from web form get method
    fullname=None
    contactaddress=None
    email=None
    phone=None
    if request.method=='GET':
        fullname = request.GET['txtName']
        contactaddress = request.GET['txtAddress']
        email = request.GET['txtEmail']
        phone = request.GET['txtPhone']
    elif request.method=='POST':
        fullname = request.POST['txtName']
        contactaddress = request.POST['txtAddress']
        email = request.POST['txtEmail']
        phone = request.POST['txtPhone']

    # Validate data
        # Server Side validation?
            # str-> functions
            # math-> functions
            # Regular Expressions (RegEx)
            # Validation-fail -> redirect to web form
            # Validation-pass -> insert record
    # Insert Record
    person1 = models.Person()
    person1.fullname=fullname
    person1.contactaddress=contactaddress
    person1.email=email
    person1.phone=phone
    result = person1.save()
    return HttpResponse("Receive data successfully")

