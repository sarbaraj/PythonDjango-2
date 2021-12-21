from django.shortcuts import render
from django.http import HttpResponse
import math

# Create your views here.

def index(request):
    # str_html =""
    # str_html+="<h1>Hello from app2</h1>"
    n1 = int(request.GET['num1'])
    n2 = int(request.GET['num2'])
    opr = request.GET['opr']
    n3 = None
    if(opr=='1'):
        n3 = n1+n2
    elif opr == '-':
        n3 = math.fabs(n1 - n2)
    elif opr == '*':
        n3 = n1 * n2
    elif opr == '/':
        n3 = n1 / n2
    return HttpResponse ("Result : {} {}".format(n3, opr))