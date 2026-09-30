from django.contrib.auth.models import AbstractUser
from django.db import models

from CailleOfWallStreet import settings


# Create your models here.


class User(AbstractUser):
    pass



class Operations(models.Model):


    name=models.CharField(max_length=200)
    price=models.FloatField(default=0.0)
    description=models.CharField(blank=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=0)
    shared=models.BooleanField(default=False)
    repeat=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)
    possible_choice=(("d","dépense"),("r","revenus"))
    type=models.CharField(max_length=7,choices=possible_choice,default="d")

    def __str__(self):
        return self.name