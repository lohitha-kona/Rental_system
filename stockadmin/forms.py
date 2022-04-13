from django import forms
from .models import AddBook,AddBicycle,AddManager,AddBike

class AddBookForm(forms.ModelForm):
	class Meta:
		model = AddBook
		exclude = ('book_id',)

class AllBooksForm(forms.ModelForm):
    allBooks=forms.ModelChoiceField(queryset=AddBook.objects.all())





class AddBicycleForm(forms.ModelForm):
	class Meta:
		model = AddBicycle
		exclude = ('bicycle_id',)

class AllBicyclesForm(forms.ModelForm):
    allBicycles=forms.ModelChoiceField(queryset=AddBicycle.objects.all())




class AddBikeForm(forms.ModelForm):
	class Meta:
		model = AddBike
		exclude = ('bike_id',)

class AllBikesForm(forms.ModelForm):
    allBooks=forms.ModelChoiceField(queryset=AddBike.objects.all())





class AddManagerForm(forms.ModelForm):
	class Meta:
		model = AddManager
		exclude = ('manager_id',)

class AllManagersForm(forms.ModelForm):
    allManagers=forms.ModelChoiceField(queryset=AddManager.objects.all())
