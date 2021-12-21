from django.shortcuts import render

def index21(request):
    # receive value from url (direct)
    tmp1 = request.GET['n1']
    tmp2 = request.GET['n2']
    # validation
        # pass
    # num1, num2
    num1 = int(tmp1)
    num2 = int(tmp2)

    # Process
    num3 = num1 + num2

    context = {'n1':num1, 'n2':num2, 'n3': num3}
    return render(request, 'app21/display1.html', context)

def index22(request):
    # receive value from url (direct)
    tmp1 = request.GET['n1']
    tmp2 = request.GET['n2']
    # validation
        # pass
    # num1, num2
    num1 = int(tmp1)
    num2 = int(tmp2)

    # Process
    num3 = num1 + num2
    
    context = {'n1':num1, 'n2':num2, 'n3': num3}
    return render(request, 'app21/display1.html', context)

# display web form
def index23(request):
    return render(request, 'app21/form1.html')

# receive data from web form
def index24(request):
    # receive value from url (direct)
    tmp1 = request.GET['n1']
    tmp2 = request.GET['n2']
    # validation
        # pass
    # num1, num2
    num1 = int(tmp1)
    num2 = int(tmp2)

    # Process
    num3 = num1 + num2
    
    context = {'n1':num1, 'n2':num2, 'n3': num3}
    return render(request, 'app21/display1.html', context)

    # receive data from web form
def index25(request):
    # receive value from url (direct)
    tmp1 = request.POST['n1']
    tmp2 = request.POST['n2']
    # validation
        # pass
    # num1, num2
    num1 = int(tmp1)
    num2 = int(tmp2)

    # Process
    num3 = num1 + num2
    
    context = {'n1':num1, 'n2':num2, 'n3': num3}
    return render(request, 'app21/display1.html', context)

def index26(request, n1, n2):
    # receive value from url (direct)
    tmp1 = n1
    tmp2 = n2
    # validation
        # pass
    # num1, num2
    num1 = int(tmp1)
    num2 = int(tmp2)

    # Process
    num3 = num1 + num2
    
    context = {'n1':num1, 'n2':num2, 'n3': num3}
    return render(request, 'app21/display1.html', context)

def index27(request):
    return render(request, 'app21/index.html')

def index28(request):
    return render(request, 'app21/index2.html')

def index29(request):
    return render(request, 'app21/index3.html')