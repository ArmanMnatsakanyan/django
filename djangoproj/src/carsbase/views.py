from django.shortcuts import render, get_object_or_404, redirect

from .models import Basa
# Create your views here.

from .forms import CarForm, RawCarForm

def cars_list_view(request):

	queryset = Basa.objects.all()
	
	context = {
		'object_list' : queryset
		}
	
	return render(request,"home.html", context)

def car_detail_view(request, id):
	car = get_object_or_404(Basa, id=id)

	context = {
		'object' : car
		}
	
	return render(request, "car.html", context)

def car_delete_view(request, id):
	car = get_object_or_404(Basa, id=id)

	if request.method == 'POST':
		car.delete()
		return redirect('../../../')
	
	context = {
		'object' : car
		}
	
	return render(request, "delete.html", context)


def car_create_view(request):

	form = CarForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = CarForm()

	context = {
		'form' : form
		}
	
	return render(request, "create.html", context)
