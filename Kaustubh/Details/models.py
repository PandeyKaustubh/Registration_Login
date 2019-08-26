from django.db import models

class details(models.Model):
   Fname=models.CharField(max_length=100)
   Lname=models.CharField(max_length=100)
   Address=models.CharField(max_length=500)
   City=models.CharField(max_length=25)
   State=models.CharField(max_length=25)
   PinCode=models.IntegerField()
   School=models.CharField(max_length=50)
   HighestQualification=models.CharField(max_length=25)
   Mobile_no=models.CharField(max_length=12)
   Email=models.CharField(max_length=100)
   Gender=models.CharField(max_length=20)



class dataTable(models.Model):

	link=models.ForeignKey(details, on_delete=models.CASCADE)
	Username=models.CharField(max_length=15)
	Password=models.CharField(max_length=25)
   