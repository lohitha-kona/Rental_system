from django.db import models
# Create your models here.

class AddBook(models.Model):
	book_id = models.AutoField(primary_key=True)
	book_name=models.CharField(max_length=1000,blank=False)
	book_author=models.CharField(max_length=1000,blank=False)
	book_edition=models.IntegerField(blank=False)
	book_cost=models.IntegerField(blank=False)
	book_stock=models.IntegerField(blank=False,default=10)
	book_location=models.ImageField(upload_to = "images/")
	class Meta:
		db_table = "addbook_table"




class AddBicycle(models.Model):
	bicycle_id = models.AutoField(primary_key=True)
	bicycle_name=models.CharField(max_length=1000,blank=False)
	bicycle_brand=models.CharField(max_length=1000,blank=False)
	bicycle_cost=models.IntegerField(blank=False)
	bicycle_stock=models.IntegerField(blank=False,default=10)
	bicycle_location=models.ImageField(upload_to = "images/")
	class Meta:
		db_table = "addbicycle_table"



class AddBike(models.Model):
	bike_id = models.AutoField(primary_key=True)
	bike_name=models.CharField(max_length=1000,blank=False)
	bike_model=models.CharField(max_length=1000,blank=False)
	bike_mil = models.IntegerField(blank=False)
	bike_cost=models.IntegerField(blank=False)
	bike_stock=models.IntegerField(blank=False,default=10)
	bike_location=models.ImageField(upload_to = "images/")
	class Meta:
		db_table = "addbike_table"




class AddManager(models.Model):
	manager_id = models.AutoField(primary_key=True)
	manager_name=models.CharField(max_length=1000,blank=False)
	manager_dob=models.CharField(max_length=10,default="00/00/0000")
	manager_email=models.CharField(max_length=1000,blank=False)
	manager_password=models.CharField(max_length=10,blank=False)
	manager_age=models.IntegerField(blank=False)
	manager_mobno=models.CharField(max_length=10,blank=False)
	manager_address=models.CharField(max_length=1000,blank=False)
	class Meta:
		db_table = "addmanager_table"