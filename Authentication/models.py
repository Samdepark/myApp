from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class  User(AbstractBaseUser):
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=100)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Username']

    def __str__(self):
        return self.usernamesername
    