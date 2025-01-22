from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

    # Fields for employees
    department = models.CharField(max_length=100, blank=True, null=True)

    def is_employee(self):
        return self.role == 'employee'

    def is_admin(self):
        return self.role == 'admin'
