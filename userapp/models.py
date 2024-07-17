from django.db import models

class MyModel(models.Model):
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)


class Lgform(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=60)




