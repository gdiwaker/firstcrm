from django.shortcuts import render
from django.http import HttpResponse

from employee.models import Employee

# Create your views here.

def homepage(request):
    employees = Employee.objects.all()
    return render(template_name='base.html', request=request, context={'employees':employees})
