from django.db import models
class fakedata(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.IntegerField()
    email=models.EmailField(max_length=100)
    city=models.CharField(max_length=100)
    dob=models.DateField(max_length=100)
    address=models.CharField(max_length=100)
