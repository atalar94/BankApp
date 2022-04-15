from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Bank(models.Model):
    name = models.CharField(max_length=255,blank=False)

    def __str__(self) -> str:
        return self.name


class Sube(models.Model):
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=False)
    kod = models.CharField(max_length=4,default=0,unique=True)

    def __str__(self) -> str:
        return self.name


class CustomUser(AbstractUser):
    account_no = models.CharField(max_length=16,blank=True,null=True)
    Sube = models.ForeignKey(Sube,on_delete=models.CASCADE,null=True)
    balance = models.IntegerField(default=0)
