from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,JsonResponse,FileResponse
from stockadmin.forms import AddBookForm,AddBicycleForm,AddBikeForm
from . forms import RegistrationForm,OrdersForm,BicycleOrdersForm,BikeOrdersForm
from stockadmin.models import AddBook,AddBicycle,AddBike
from . models import Registration,Orders,BicycleOrders,BikeOrders
from project.settings import MEDIA_ROOT, MEDIA_URL
from django.db.models import Q
from django.core.mail import EmailMessage
from django.conf import settings
import pytest
from django.contrib.auth.modelsimport User

def registration(request):
	if request.method == 'POST':
		user_uname = request.POST['user_uname']
		pwd = request.POST['user_pwd']
		form = RegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			flag = Registration.objects.filter(Q(user_uname__iexact=user_uname) & Q(user_pwd__iexact=pwd))
			if flag:
				email = Registration.objects.get(user_uname=user_uname).user_email
				request.session['email'] = email
				# subject="Rent Successful- From LAYers"
				subject = "LAYers confirmation mail"
				msg1 = " Please click on this link to verify your mail : http://127.0.0.1:8000/confirmlogin/ "
				email = email
				email = EmailMessage(subject, msg1, to=[email])  # to will take list of email IDs
				email.send()
			return render(request, 'confirmation.html')
	else:
		form = RegistrationForm()
	return render(request, 'Registration.html', {'form': form})


def userlogin(request):
	return render(request, "userlogin.html")


def userchecklogin(request):
	if request.method == 'POST':
		user_uname = request.POST['uname']
		pwd = request.POST['pwd']
		request.session['user_uname'] = user_uname
		flag = Registration.objects.filter(Q(user_uname__iexact=user_uname) & Q(user_pwd__iexact=pwd) & Q(status=True))
		if flag:
			return render(request, "userhome.html", {'user_uname': user_uname})
		else:
			return HttpResponse("Verify your mail")
	else:
		return render(request, 'userlogin.html')


def userconfirmlogin(request):
	if request.method == 'POST':
		user_uname = request.POST['uname']
		pwd = request.POST['pwd']
		request.session['user_uname'] = user_uname
		Registration.objects.filter(Q(user_uname__iexact=user_uname) & Q(user_pwd__iexact=pwd)).update(status=True)
		flag = Registration.objects.filter(Q(user_uname__iexact=user_uname) & Q(user_pwd__iexact=pwd))
		if flag:
			return render(request, "userhome.html", {'user_uname': user_uname})
	else:
		return render(request, 'confirmlogin.html')


def confirmlogin(request):
	return render(request, "confirmlogin.html")

def userhome(request):
  user_uname=request.session['user_uname']
  return render(request,"userhome.html",{'user_uname':user_uname})

def rentabook(request):
  user_uname=request.session['user_uname']
  print(user_uname)
  books = AddBook.objects.all()
  return render(request,"rentabook.html",{'books':books,'user_uname':user_uname})

def renting(request,book_id,book_name,book_cost,book_stock):
  user_uname=request.session['user_uname']
  print("user",user_uname)
  request.session['book_id']=book_id
  request.session['book_name']=book_name
  request.session['book_cost']=book_cost
  request.session['book_stock']=book_stock
  email=Registration.objects.get(user_uname=user_uname).user_email
  if request.method == 'POST':
    form = OrdersForm(request.POST)
    form.save()
    book_id=request.session['book_id']
    if(book_stock>0):
      flag=AddBook.objects.filter(book_id=book_id).update(book_stock=book_stock-1)
      request.session['email']=email
      #subject="Rent Successful- From LAYers"
      subject=book_name,"with",book_cost,"Is rented Successfully"
      msg1="Thank u for renting from our wesite!!!"
      email=email
      email=EmailMessage(subject,msg1,to=[email])  #to will take list of email IDs
      email.send()
      return render(request, 'rentingsuccess.html', {'alert_flag': True})
    else:
      return HttpResponse("Stock Unavailable")
      return render(request,'userhome.html',{'user_uname',user_uname})
  else:
    form = OrdersForm()
  return render(request,"renting.html",{'form':form,'user_uname':user_uname,'book_id':book_id,'book_name':book_name,'book_cost':book_cost,'book_stock':book_stock})



def rentabicycle(request):
  user_uname=request.session['user_uname']
  print(user_uname)
  bicycles = AddBicycle.objects.all()
  return render(request,"rentabicycle.html",{'bicycles':bicycles,'user_uname':user_uname})

def renting2(request,bicycle_id,bicycle_name,bicycle_cost,bicycle_stock):
  user_uname=request.session['user_uname']
  print("user",user_uname)
  request.session['bicycle_id']=bicycle_id
  request.session['bicycle_name']=bicycle_name
  request.session['bicycle_cost']=bicycle_cost
  request.session['bicycle_stock']=bicycle_stock
  if request.method == 'POST':
    form = BicycleOrdersForm(request.POST)
    if form.is_valid():
      form.save()
      bicycle_id=request.session['bicycle_id']
      if(bicycle_stock>0):
        flag=AddBicycle.objects.filter(bicycle_id=bicycle_id).update(bicycle_stock=bicycle_stock-1)
        return render(request,"rentingsuccess.html")
      else:
        return HttpResponse("Stock Unavailable")
      return render(request,'userhome.html',{'user_uname',user_uname})
  else:
    form = BicycleOrdersForm()
  return render(request,"renting2.html",{'form':form,'user_uname':user_uname,'bicycle_id':bicycle_id,'bicycle_name':bicycle_name,'bicycle_cost':bicycle_cost,'bicycle_stock':bicycle_stock})


def rentabike(request):
  user_uname=request.session['user_uname']
  print(user_uname)
  bikes = AddBike.objects.all()
  return render(request,"rentabike.html",{'bikes':bikes,'user_uname':user_uname})

def rentingbike(request,bike_id,bike_name,bike_cost,bike_stock):
  user_uname=request.session['user_uname']
  print("user",user_uname)
  request.session['bike_id']=bike_id
  request.session['bike_name']=bike_name
  request.session['bike_cost']=bike_cost
  request.session['bike_stock']=bike_stock
  if request.method == 'POST':
    form = BikeOrdersForm(request.POST)
    if form.is_valid():
      form.save()
      bike_id=request.session['bike_id']
      if(bike_stock>0):
        flag=AddBike.objects.filter(bike_id=bike_id).update(bike_stock=bike_stock-1)
        return render(request,"rentingsuccess.html")
      else:
        return HttpResponse("Stock Unavailable")
      return render(request,'userhome.html',{'user_uname',user_uname})
  else:
    form = BicycleOrdersForm()
  return render(request,"rentingbike.html",{'form':form,'user_uname':user_uname,'bike_id':bike_id,'bike_name':bike_name,'bike_cost':bike_cost,'bike_stock':bike_stock})
