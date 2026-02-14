from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    hire_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
