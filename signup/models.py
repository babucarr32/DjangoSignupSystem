from django.db import models


class signupModel(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)