from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role
from datetime import datetime

def add_emp(request):
    if request.method == 'POST':
        try:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            salary = int(request.POST.get('salary'))
            bonus = int(request.POST.get('bonus'))
            phone = int(request.POST.get('phone'))
            dept = int(request.POST.get('dept'))
            role = int(request.POST.get('role'))

            new_emp = Employee(
                first_name=first_name,
                last_name=last_name,
                salary=salary,
                bonus=bonus,
                phone=phone,
                dept_id=dept,
                role_id=role,
                hire_date=datetime.now()
            )
            new_emp.save()

            return HttpResponse("Employee Added Successfully ✅")

        except Exception as e:
            return HttpResponse(f"Error: {e}")

    elif request.method == 'GET':
        departments = Department.objects.all()
        roles = Role.objects.all()

        context = {
            'departments': departments,
            'roles': roles
        }

        return render(request, 'add_emp.html', context)

    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")
