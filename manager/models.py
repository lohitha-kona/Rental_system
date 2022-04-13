from django.db import models

# Create your models here.
class AddStaff(models.Model):
	staff_id = models.AutoField(primary_key=True)
	staff_name=models.CharField(max_length=1000,blank=False)
	staff_dob=models.CharField(max_length=10,default="00/00/0000")
	staff_email=models.CharField(max_length=1000,blank=False)
	staff_password=models.CharField(max_length=10,blank=False)
	staff_age=models.IntegerField(blank=False)
	staff_mobno=models.CharField(max_length=10,blank=False)
	staff_address=models.CharField(max_length=1000,blank=False)
	class Meta:
		db_table = "addstaff_table"