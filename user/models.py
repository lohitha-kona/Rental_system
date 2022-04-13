from django.db import models

# Create your models here.

class Registration(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_fname=models.CharField(max_length=1000,blank=False)
	user_email=models.EmailField(max_length=1000,blank=False)
	user_uname=models.CharField(max_length=1000,blank=False)
	user_pwd=models.CharField(max_length=1000,blank=False)
	user_mob=models.CharField(max_length=10,blank=False)
	user_add=models.CharField(max_length=1000,blank=False)
	class Meta:
		db_table = "users_table"

class Orders(models.Model):
	order_id=models.AutoField(primary_key=True)
	fname=models.CharField(max_length=1000,blank=False)
	bname=models.CharField(max_length=1000,blank=False)
	bcost=models.IntegerField(blank=False)
	category_choices = (('Programming','Programming'),('Entertainment','Entertainment'),('Others','Others'))
	book_category=models.CharField(max_length=50,choices=category_choices,blank=False)
	order_date=models.DateTimeField(auto_now=True)
	mob=models.CharField(max_length=10,blank=False)
	add=models.CharField(max_length=10000,blank=False)
	staff_id=models.IntegerField(default=0)
	num=models.IntegerField(default=0)
	class Meta:
		db_table="orders_table"


class BicycleOrders(models.Model):
	order_id=models.AutoField(primary_key=True)
	cname=models.CharField(max_length=1000,blank=False)
	bcname=models.CharField(max_length=1000,blank=False)
	bccost=models.IntegerField(blank=False)
	category_choices = (('sports','sports'),('road','road'),('Others','Others'))
	bicycle_category=models.CharField(max_length=50,choices=category_choices,blank=False)
	order_date=models.DateTimeField(auto_now=True)
	mob=models.CharField(max_length=10,blank=False)
	add=models.CharField(max_length=10000,blank=False)
	staff_id=models.IntegerField(default=0)
	num=models.IntegerField(default=0)
	class Meta:
		db_table="bicycleorders_table"




class BikeOrders(models.Model):
	order_id=models.AutoField(primary_key=True)
	cname=models.CharField(max_length=1000,blank=False)
	bkname=models.CharField(max_length=1000,blank=False)
	bkmodel=models.CharField(max_length=1000,blank=False)
	bkmil=models.IntegerField(blank=False)
	bkcost=models.IntegerField(blank=False)
	category_choices = (('sports','sports'),('road','road'),('Others','Others'))
	bike_category=models.CharField(max_length=50,choices=category_choices,blank=False)
	order_date=models.DateTimeField(auto_now=True)
	mob=models.CharField(max_length=10,blank=False)
	add=models.CharField(max_length=10000,blank=False)
	staff_id=models.IntegerField(default=0)
	num=models.IntegerField(default=0)
	class Meta:
		db_table="bikeorders_table"