from django.shortcuts import render, HttpResponse, redirect
from .models import Ninja, Dojo


def index(request):

	context = {
		"all_the_dojos": Dojo.objects.all(),
		"all_the_ninjas": Ninja.objects.all()
	}
	
	return render(request, 'index.html', context)


def add_user(request):

	Ninja.objects.create(
		dojo_id = Dojo.objects.get(id=request.POST['ninja_dojo_select']),
		first_name = request.POST['ninja_first_name_input'],
		last_name = request.POST['ninja_last_name_input'],

	)

	return redirect('/')


def add_dojo(request):

	Dojo.objects.create(

		name = request.POST['dojo_name_input'],
		city = request.POST['dojo_city_input'],
		state = request.POST['dojo_state_input']

	)

	return redirect('/')