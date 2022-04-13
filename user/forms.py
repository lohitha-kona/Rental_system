from django import forms
from .models import Registration,Orders,BicycleOrders,BikeOrders

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Registration
		exclude = ('user_id',)

class OrdersForm(forms.ModelForm):
	class Meta:
		model=Orders
		exclude=('order_id','order_date','staff_id','num',)

class BicycleOrdersForm(forms.ModelForm):
	class Meta:
		model=BicycleOrders
		exclude=('order_id','order_date','staff_id','num',)

class BikeOrdersForm(forms.ModelForm):
	class Meta:
		model=BikeOrders
		exclude=('order_id','order_date','staff_id','num',)