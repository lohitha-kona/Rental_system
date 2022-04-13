# Create your views here.
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,JsonResponse,FileResponse
from django.db.models import Q, Max  # where Q is Query Set
from stockadmin.models import AddManager
from . forms import AddStaffForm
from . models import AddStaff
from user.forms import OrdersForm,BicycleOrdersForm,BikeOrdersForm
from user.models import Orders,BicycleOrders,BikeOrders
import random


def managerlogin(request):
	#return render(request,"managerhome.html")
	if request.method == "POST":
		email = request.POST["email"]
		pwd = request.POST["pwd"]
		if AddManager.objects.filter(manager_email=email,manager_password=pwd).exists():
			return render(request,"managerhome.html")
		else:
			#return render(request,"managerlogin.html")
			return HttpResponse("Login Invalid")
	else:
		return render(request,"managerlogin.html")

def managerhome(request):
	return render(request,"managerhome.html")






def addstaff(request):
	if request.method == 'POST':
		form = AddStaffForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			#return render(request,'adminhome.html')
			return redirect("/viewstaff")  
	else:
		form = AddStaffForm()
	return render(request,'addstaff.html',{'form':form})

def viewstaff(request):  
    staff = AddStaff.objects.all()  
    return render(request,"viewstaff.html",{'staff':staff}) 

def deletestaff(request,id):  
    staff= AddStaff.objects.get(staff_id=id)  
    staff.delete()  
    return redirect("/viewstaff")  



def viewbookorders(request):
	orders = Orders.objects.all()
	return render(request,"viewbookorders.html",{'orders':orders})

def updatebookorders(request,order_id):
	request.session["order_id"]=order_id
	id=AddStaff.objects.all().aggregate(Max('staff_id'))
	n = random.randint(1,id.values()) # returns a random integer
	Orders.objects.filter(order_id=order_id).update(staff_id=n)
	return redirect("/viewbookorders") 


def viewbicycleorders(request):
	orders = BicycleOrders.objects.all()
	return render(request,"viewbicycleorders.html",{'orders':orders})

def updatebicycleorders(request,order_id):
	request.session["order_id"]=order_id
	n = random.randint(1,5) # returns a random integer
	BicycleOrders.objects.filter(order_id=order_id).update(staff_id=n)
	return redirect("/viewbicycleorders") 


def viewbikeorders(request):
	orders = BikeOrders.objects.all()
	return render(request,"viewbikeorders.html",{'orders':orders})

def updatebikeorders(request,order_id):
	request.session["order_id"]=order_id
	n = random.randint(1,5) # returns a random integer
	BikeOrders.objects.filter(order_id=order_id).update(staff_id=n)
	return redirect("/viewbikeorders") 


    

def mviewdeliveries(request):
	deliveries=Orders.objects.filter(num=0)
	return render(request,"mviewdeliveries.html",{'deliveries':deliveries})

def mviewreturns(request):
	returns=Orders.objects.filter(num=1)
	return render(request,"mviewreturns.html",{'returns':returns})
