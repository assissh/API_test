from django.db import models

# Create your models here.
class User_Profile(models.Model):
    Name = models.CharField(max_length=20,default=False)
    First_Name = models.CharField(max_length=10,default=False)
    Last_Name = models.CharField(max_length=10,default=False)
    Fathers_Name = models.CharField(max_length=20,default=False)
    Mothers_Name = models.CharField(max_length=20,default=False)
    Address = models.CharField(max_length=30,default=False)
    City = models.CharField(max_length=10,default=False)
    Pin_Code = models.IntegerField(default=False)
    Phone_No = models.IntegerField(default=False)
    Education = models.CharField(max_length=10,default=False)

    def __str__(self):
        return self.Name