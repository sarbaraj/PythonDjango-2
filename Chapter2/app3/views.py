from django.db.models.base import Model
from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    # Get all records from table
    all_persons = models.Person.objects.all()
    # send records to template (index.html)
    return render(request, 'app3/index.html', 
        {'persons':all_persons})

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

def displayedit(request):
    pid = request.GET['pid'] # getting pid from url
    # search record on database
    person = models.Person.objects.get(id=pid)
    return render(request, 'app3/displayedit.html', 
        {'person':person})
    
def receiveedit(request):
    # Receive record from form
    pid = request.POST['txtID']
    fullname = request.POST['txtName']
    contactaddress = request.POST['txtAddress']
    email = request.POST['txtEmail']
    phone = request.POST['txtPhone']

    # getting record from database
    person = models.Person.objects.get(id=pid)
    
    # update record
    # set new values
    person.fullname=fullname
    person.contactaddress=contactaddress
    person.email=email
    person.phone=phone
    # save record
    person.save()
    return HttpResponse("Reccord update successfully!")

def displaydelete(request):
    return HttpResponse("Display delete")

