from django.shortcuts import render
from django.http import HttpResponse
from employeee.models import Employee

def home(request):
    employee = Employee.objects.all()
    context = {
        'employee': employee,
    }
    return render(request,"index.html",context)