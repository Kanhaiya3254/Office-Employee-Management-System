from django.shortcuts import render, redirect
from .models import Employee, Role, Department

def index(request):
    return render(request, 'index.html')

def add_emp(request):
    roles = Role.objects.all()
    depts = Department.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        role_id = request.POST.get('role')
        dept_id = request.POST.get('dept')

        emp = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            role=Role.objects.get(id=role_id),
            dept=Department.objects.get(id=dept_id)
        )
        emp.save()
        return redirect('all_emp')
    context = {'roles': roles, 'depts': depts}
    return render(request, 'add_emp.html', context)

def all_emp(request):
    emps = Employee.objects.all()
    return render(request, 'all_emp.html', {'emps': emps})

def remove_emp(request):
    emps = Employee.objects.all()
    return render(request, 'remove_emp.html', {'emps': emps})

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(first_name__icontains=name) | emps.filter(last_name__icontains=name)
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)
        return render(request, 'filter_emp.html', {'emps': emps, 'name': name, 'dept': dept, 'role': role})
    return render(request, 'filter_emp.html')
