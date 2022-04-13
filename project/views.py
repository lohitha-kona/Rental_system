from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,JsonResponse,FileResponse


def indexfunction(request):
	return render(request,"index.html")
