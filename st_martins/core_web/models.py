from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class Contact(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(blank=False, null=True)
    message = models.TextField(blank=False, null=True)

    def __str__(self):
        return self.name


