from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name

    __str__ = __repr__


class Employee(models.Model):
    fullname = models.CharField(max_length=128)
    employee_id = models.CharField(max_length=6)
    phone = models.CharField(max_length=16, null=True, blank=True)
    joined_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __repr__(self):
        return '{} <{}>'.format(self.fullname, self.employee_id)

    __str__ = __repr__
