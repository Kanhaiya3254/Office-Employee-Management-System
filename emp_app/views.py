from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role
from datetime import datetime


def add_emp(request):
    if request.method == "POST":
        try:
            # Get form data
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            salary = request.POST.get("salary")
            bonus = request.POST.get("bonus")
            phone = request.POST.get("phone")
            dept_id = request.POST.get("dept")
            role_id = request.POST.get("role")

            # Validation check
            if not all([first_name, last_name, salary, bonus, phone, dept_id, role_id]):
                return HttpResponse("⚠ All fields are required!")

            # Get Department and Role objects safely
            dept = Department.objects.get(id=int(dept_id))
            role = Role.objects.get(id=int(role_id))

            # Create Employee
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

        except Department.DoesNotExist:
            return HttpResponse("❌ Selected Department does not exist!")

        except Role.DoesNotExist:
            return HttpResponse("❌ Selected Role does not exist!")

        except ValueError:
            return HttpResponse("❌ Salary, Bonus and Phone must be numbers!")

        except Exception as e:
            return HttpResponse(f"❌ Error: {e}")

    # GET request
    departments = Department.objects.all()
    roles = Role.objects.all()

    context = {
        "departments": departments,
        "roles": roles
    }

    return render(request, "add_emp.html", context)
