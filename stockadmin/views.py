# Create your views here.
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,JsonResponse,FileResponse
from django.db.models import Q  #where Q is Query Set
from . forms import AddBookForm,AddBicycleForm,AddBikeForm,AddManagerForm
from . models import AddBook,AddBicycle,AddBike,AddManager



def adminlogin(request):
	if request.method == "POST":
		uname = request.POST["uname"]
		pwd = request.POST["pwd"]
		flag1 = uname == '190030490' and pwd == 'gayathri'
		flag2 = uname == '190030030' and pwd == 'siri'
		flag3 = uname == '190030826' and pwd == 'lohitha'
		if flag1:
			return render(request,"adminhome.html")
		elif flag2:
			return render(request,"adminhome.html")
		elif flag3:
			return render(request,"adminhome.html")
		else:
			return HttpResponse("Login Invalid")
	else:
		return render(request,"adminlogin.html")


def adminhome(request):
	return render(request,"adminhome.html")






def adminaddbook(request):
	if request.method == 'POST':
		form = AddBookForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			#return render(request,'adminhome.html')
			return redirect("/viewbooks")  
	else:
		form = AddBookForm() 
	return render(request,'addbook.html',{'form':form})

def viewbooks(request):  
    books = AddBook.objects.all()  
    return render(request,"viewbooks.html",{'books':books}) 
def deletebooks(request,id):  
    book= AddBook.objects.get(book_id=id)  
    book.delete()  
    return redirect("/viewbooks")  
def updatebooks(request,book_name,book_edition):
    request.session["book_name"] = book_name
    request.session["book_edition"] = book_edition
    return render(request,'updatebook.html',{'book_name':book_name,'book_edition':book_edition})

def updatebookdetails(request):
    if request.method == "POST":
        book_name = request.session["book_name"]
        book_edition = request.session["book_edition"]
        stock=request.POST["bs"]
        AddBook.objects.filter(book_name=book_name,book_edition=book_edition).update(book_stock=stock)
        return render(request,"adminhome.html")
    else:
        return HttpResponse("Error")






def addbicycle(request):
	if request.method == 'POST':
		form = AddBicycleForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			#return render(request,'adminhome.html')
			return redirect("/viewbicycles")  
	else:
		form = AddBicycleForm()
	return render(request,'addbicycle.html',{'form':form})

def viewbicycles(request):  
    bicycles = AddBicycle.objects.all()  
    return render(request,"viewbicycles.html",{'bicycles':bicycles}) 
def deletebicycles(request,id):  
    bicycle= AddBicycle.objects.get(bicycle_id=id)  
    bicycle.delete()  
    return redirect("/viewbicycles")  
def updatebicycles(request,bicycle_name,bicycle_brand):
    request.session["bicycle_name"] = bicycle_name
    request.session["bicycle_brand"] = bicycle_brand
    return render(request,'updatebicycle.html',{'bicycle_name':bicycle_name,'bicycle_brand':bicycle_brand})

def updatebicycledetails(request):
    if request.method == "POST":
        bicycle_name = request.session["bicycle_name"]
        bicycle_brand = request.session["bicycle_brand"]
        stock=request.POST["bs"]
        AddBicycle.objects.filter(bicycle_name=bicycle_name,bicycle_brand=bicycle_brand).update(bicycle_stock=stock)
        return render(request,"adminhome.html")
    else:
        return HttpResponse("Error")






def adminaddbike(request):
	if request.method == 'POST':
		form = AddBikeForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect("/viewbikes")
	else:
		form = AddBikeForm()
	return render(request,'addbike.html',{'form':form})
def viewbikes(request):
    bikes = AddBike.objects.all()
    return render(request,"viewbikes.html",{'bikes':bikes})

def deletebikes(request,id):
    bike= AddBike.objects.get(bike_id=id)
    bike.delete()
    return redirect("/viewbikes")

def updatebikes(request,bike_name,bike_model):
    request.session["bike_name"] = bike_name
    request.session["bike_model"] = bike_model
    return render(request,'updatebike.html',{'bike_name':bike_name,'bike_model':bike_model})

def updatebikedetails(request):
    if request.method == "POST":
        bike_name = request.session["bike_name"]
        bike_model = request.session["bike_model"]
        stock=request.POST["bs"]
        AddBike.objects.filter(bike_name=bike_name,bike_model=bike_model).update(bike_stock=stock)
        return render(request,"adminhome.html")
    else:
        return HttpResponse("Error")








def addmanager(request):
	if request.method == 'POST':
		form = AddManagerForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			#return render(request,'adminhome.html')
			return redirect("/viewmanagers")  
	else:
		form = AddManagerForm()
	return render(request,'addmanager.html',{'form':form})

def viewmanagers(request):  
    managers = AddManager.objects.all()  
    return render(request,"viewmanagers.html",{'managers':managers}) 

def deletemanagers(request,id):  
    manager= AddManager.objects.get(manager_id=id)  
    manager.delete()  
    return redirect("/viewmanagers")  