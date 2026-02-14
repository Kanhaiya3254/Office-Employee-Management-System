from django.shortcuts import render, redirect
from .models import Employee, Role, Department


def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = Role.objects.get(id=request.POST['role'])
        dept = Department.objects.get(id=request.POST['dept'])

        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            role=role,
            dept=dept
        )

        return redirect('all_emp')

    roles = Role.objects.all()
    depts = Department.objects.all()

    return render(request, 'add_emp.html', {'roles': roles, 'depts': depts})


def remove_emp(request, emp_id=None):
    if emp_id:
        emp = Employee.objects.get(id=emp_id)
        emp.delete()
        return redirect('all_emp')

    emps = Employee.objects.all()
    return render(request, 'remove_emp.html', {'emps': emps})
