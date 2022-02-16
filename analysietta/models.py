from django.db import models
import datetime

class Users(models.Model):
    email = models.EmailField(max_length=50, default="", null=False)
    password = models.CharField(max_length=100, default="", null=False)

class Income(models.Model):
    user_id = models.IntegerField(null=False)
    type = models.IntegerField(null=False)
    date = models.DateField(default=datetime.date.today, null=False)
    money = models.IntegerField(null=False)

class Cost(models.Model):
    user_id = models.IntegerField(null=False)
    type = models.IntegerField(null=False)
    date = models.DateField(default=datetime.date.today, null=False)
    money = models.IntegerField(null=False)
