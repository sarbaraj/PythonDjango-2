from django.shortcuts import render

# Create your views here.

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
    return render(request, 'app22/body.html')
