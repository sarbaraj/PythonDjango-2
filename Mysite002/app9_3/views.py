from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Form Save")
                return HttpResponseRedirect('../show')
            except:
                pass
    else:
        form = EmployeeForm()
        return render(request,'app9_3/index.html',{'form':form})


def show(request):
    employees = Employee.objects.all()
    print(employees)
    return render(request,"app9_3/show.html",{'employees':employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    print(employee)
    return render(request,'app9_3/edit.html', {'employee':employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('../show')
    return render(request, 'app9_3/edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return HttpResponseRedirect('../show')