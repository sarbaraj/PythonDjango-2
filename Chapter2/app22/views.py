from django.http.response import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    str_html="<h2>Links</h2>"
    str_html+="<p><a href='app1'>Link-1</a></p>" # href= url pattern
    str_html+="<p><a href='app21/displayform'>Link-2</a></p>"
    str_html+="<p><a href='displayform1'>Link-3</a></p>"
    str_html+="<p><a href='sendvalue1'>Link-4</a></p>"
    return HttpResponse(str_html)

def index220(request):
    return render(request, 'app22/form1.html')

def index221(request):
    #receive
    # tmp1 = request.GET['n1']
    # tmp2 = request.GET['n2']
    # validation
    # process
    # n3 = int(tmp1)+int(tmp2)
    # packaging
    # context = {'n3':n3}
    
    # autoscape
    """
    str1 ="<h2>Autoescape Example</h2>"
    context = {'str1': str1}
    return render(request, 'app22/index.html', context)
    """
    # csrf_token
    """
    txtUser=None
    txtPass=None
    txtKey = None
    if request.method =='GET':
        txtUser = request.GET['txtUser']
        txtPass = request.GET['txtPass']
    elif request.method=='POST':
        txtUser = request.POST['txtUser']
        txtPass = request.POST['txtPass']
        txtKey = request.POST['csrfmiddlewaretoken']
    result="Error user name or password"
    if(txtUser=='admin' and txtPass=='admin'):
        result="Welcome {} !".format(txtUser)
    context={'user': txtUser, 'pass':txtPass, 'remarks': result, 'key':txtKey}
    return render(request, 'app22/index.html', context)
    """
    # cycle & filter
    """
    list1 = ["raj",'kiran','keshor','sishir']
    context = {'nums':list1}
    return render(request, 'app22/index.html', context)
    """

    # firstof
    """
    var1 = None
    var2 = None
    var3 = None
    context = {'n1':var1, 'n2':var2, 'n3':var3}
    return render(request, 'app22/index.html', context)
    """

    # autoscape
    # for

    #if
    """
    context = {'sub1':34, 'sub2':54, 'PM':40}
    return render(request, 'app22/index.html', context)
    """

    # extends, block
    """
    return render(request, 'app22/body.html')
    """

    # filters
    # context  ={'num1':45}
    # return render(request, 'app22/index.html', context)

    # 
    """
    context  ={'str1':'I "cant" do this'}
    return render(request, 'app22/index.html', context)
    """
    # capfirst # center
    """
    context={'str1':'broadway infosys nepal'}
    return render(request, 'app22/index.html', context)
    """

    # date
    """
    current_dt = datetime.datetime.now()
    context={'str1':current_dt}
    return render(request, 'app22/index.html', context)
    """

    # default | default_if_none
    """
    var1 = None
    context={'str1':var1}
    return render(request, 'app22/index.html', context)
    """
    # dictsort
    """
    dict1 =[
        {'name': 'zed', 'age': 19},
        {'name': 'amy', 'age': 22},
        {'name': 'joe', 'age': 31},
    ]
    context={'var1':dict1}
    return render(request, 'app22/index.html', context)
    """

    # floatformat
    context={'var1':123.4567890}
    return render(request, 'app22/index.html', context)
