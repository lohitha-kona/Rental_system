from django import forms
from .models import AddStaff


class AddStaffForm(forms.ModelForm):
	class Meta:
		model = AddStaff
		exclude = ('staff_id',)

class AllStaffForm(forms.ModelForm):
    allStaff=forms.ModelChoiceField(queryset=AddStaff.objects.all())
