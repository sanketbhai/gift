from django.db import models

# Create your models here.
class Records(models.Model):
    Sender = models.CharField(max_length=30)
    Receiver = models.CharField(max_length=30)
    Hint=models.CharField(max_length=300)
    Password=models.CharField(max_length=300)
