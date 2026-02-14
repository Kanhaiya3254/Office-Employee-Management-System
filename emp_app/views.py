from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role
from datetime import datetime


# ✅ Home Page
def index(request):
    return render(request, "index.html")


# ✅ View All Employees
def all_emp(request):
    emps = Employee.objects.all()
    return render(request, "all_emp.html", {"emps": emps})


# ✅ Add Employee
def add_emp(request):
    if request.method == "POST":
        try:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            salary = request.POST.get("salary")
            bonus = request.POST.get("bonus")
            phone = request.POST.get("phone")
            dept_id = request.POST.get("dept")
            role_id = request.POST.get("role")

            if not all([first_name, last_name, salary, bonus, phone, dept_id, role_id]):
                return HttpResponse("⚠ All fields are required!")

            dept = Department.objects.get(id=int(dept_id))
            role = Role.objects.get(id=int(role_id))

            new_emp = Employee(
                first_name=first_name,
                last_name=last_name,
                salary=int(salary),
                bonus=int(bonus),
                phone=int(phone),
                dept=dept,
                role=role,
                hire_date=datetime.now()
            )

            new_emp.save()
            return HttpResponse("✅ Employee Added Successfully!")

        except Exception as e:
            return HttpResponse(f"❌ Error: {e}")

    departments = Department.objects.all()
    roles = Role.objects.all()

    return render(request, "add_emp.html", {
        "departments": departments,
        "roles": roles
    })
