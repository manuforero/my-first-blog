from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import loader
from django.shortcuts import render, get_object_or_404

from .models import Receta
from .forms import RecetForm

# Create your views here.
def hello_mundo(request):
	receta_org = Receta.objects.order_by('id')
	template = loader.get_template('index.html')
	context = {
		'recetitas': receta_org
	}
	return HttpResponse(template.render(context, request))
	

def recet_detail(request, pk):
	recetad =  get_object_or_404(Receta, pk=pk)
	template = loader.get_template('recet_detail.html')
	context = {
		'receta_detalles': recetad
	}
	return HttpResponse(template.render(context, request))

def new_recipe(request):
	if request.method == 'POST':
		form = RecetForm(request.POST, request.FILES)
		if form.is_valid():
			receta = form.save(commit = False)
			receta.save()
			return HttpResponseRedirect('/')
	else:
		form = RecetForm()

	template = loader.get_template('new_recipe.html')
	context = {
		'form' : form
	}
	return HttpResponse(template.render(context, request))
