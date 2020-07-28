from django import forms

from .models import Basa

class CarForm(forms.ModelForm):
	manufacturer = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'производитель'}))
	model        = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'модель'}))
	drivable     = forms.BooleanField()
	seats_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'посадочных мест'}))
	year         = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'произведено в таком-то году'}))
	class Meta:
		model = Basa
		fields = [
			'manufacturer',
			'model',
			'drivable',
			'seats_number',
			'year',
		]


class RawCarForm(forms.Form):
	manufacturer = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'производитель'}))
	model        = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'модель'}))
	drivable     = forms.BooleanField()
	seats_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'посадочных мест'}))
	year         = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'произведено в таком-то году'}))