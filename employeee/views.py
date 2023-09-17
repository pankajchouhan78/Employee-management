from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse, Http404
from . models import Employee
# Create your views here.
# def employee_details(request,pk):
#     try:
#         emp = Employee.objects.get(pk = pk)
#         return HttpResponse(emp)
#     except:
#         return Http404

def employee_details(request,pk):
    emp = get_object_or_404(Employee,pk=pk)
    # return HttpResponse(emp)
    context = {
        'employee': emp,
    }
    return render(request,"employee_detail.html",context)