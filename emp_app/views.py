from django.shortcuts import render, redirect
from .models import Employee


def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'all_emp.html', context)


def remove_emp(request, emp_id=None):
    if emp_id:
        try:
            emp = Employee.objects.get(id=emp_id)
            emp.delete()
            return redirect('all_emp')
        except:
            return redirect('remove_emp')

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)
