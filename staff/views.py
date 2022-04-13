# Create your views here.
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,JsonResponse,FileResponse
from django.db.models import Q  #where Q is Query Set
from manager.models import AddStaff
from stockadmin.models import AddBook
from user.models import Orders

def stafflogin(request):
	if request.method == "POST":
		email = request.POST["email"]
		pwd = request.POST["pwd"]
		staff_id = AddStaff.objects.get(staff_password=pwd).staff_id
		request.session['staff_id']=staff_id
		if AddStaff.objects.filter(staff_email=email,staff_id=staff_id).exists():
			return render(request,"staffhome.html",{'staff_id':staff_id})
		else:
			#return render(request,"managerlogin.html")
			return HttpResponse("Login Invalid")
	else:
		return render(request,"stafflogin.html")

def staffhome(request):
	staff_id=request.session['staff_id']
	return render(request,"staffhome.html")



def viewtaskscompleted(request):
	staff_id=request.session['staff_id']
	tasks=Orders.objects.filter(num=2,staff_id=staff_id)
	return render(request,"viewtaskcompleted.html",{'tasks':tasks,'staff_id':staff_id})

def viewdeliveries(request):
	staff_id =request.session['staff_id']
	deliveries=Orders.objects.filter(num=0,staff_id=staff_id)
	return render(request,"viewdeliveries.html",{'deliveries':deliveries,'staff_id':staff_id})

def viewreturns(request):
	staff_id = request.session['staff_id']
	returns=Orders.objects.filter(num=1,staff_id=staff_id)
	return render(request,"viewreturns.html",{'returns':returns,'staff_id':staff_id})

def delivered(request,order_id):
	request.session["order_id"] = order_id
	staff_password= 22/22/2222
	staff_id =2
	Orders.objects.filter(order_id=order_id).update(num=1)
	return redirect("/viewreturns")

def returned(request,order_id,bname):
  request.session["order_id"] = order_id
  request.session["bname"] = bname
  #staff_password= 22/22/2222
  #staff_id =2
  flag=AddBook.objects.filter(book_name=bname)
  if flag:
    s=AddBook.objects.get(book_name=bname).book_stock
    #bn=AddBook.objects.filter(book_name=bname).book_id
    flag=AddBook.objects.filter(book_name=bname).update(book_stock=s+1)
    flag1=Orders.objects.filter(order_id=order_id).update(num=2)
    return redirect("/viewtaskscompleted")
  else:
    return HttpResponse("Book Does not Exist")
  return render(request,"viewreturns.html")
