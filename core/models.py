from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, related_name='roles', on_delete=models.CASCADE)

    def __str__(self):
        return "Name: " + self.user.username + ", Role: " + self.role.name

