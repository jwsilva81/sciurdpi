from django.shortcuts import render
from core.models import Pastor, Esposa, Filho, Igreja, Carro
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
#from core.forms import PastorForm, EsposaForm, FilhoForm,IgrejaForm, CarroForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

#PASTOR

class HomeView(TemplateView):
	template_name = 'index.html'


class PastorListView(ListView):
	template_name = 'view.html'
	model = Pastor
	#context_object_name = 'nome,' 'cpf'
		

class PastorDetailView(DetailView):
	 template_name = 'detail.html'
	 model = Pastor
	
class PastorCreateView(CreateView):
	template_name = 'add.html'
	model = Pastor
	success_url = reverse_lazy('listar')


class PastorUpdateView(UpdateView):
	template_name = 'update.html'
	model = Pastor
	success_url = '/pastor/'


class PastorDeleteView(DeleteView):
	template_name = 'delete.html'
	model = Pastor
	success_url  = reverse_lazy('pastor-list')


#Esposa	
class EsposaListView(ListView):
	model = Esposa
	success_url = reverse_lazy('listar')


class EsposaDetailView(DetailView):
	model = Esposa


class EsposaCreateView(CreateView):
	template_name = 'esposa.html'
	model = Esposa
	success_url =  reverse_lazy('esposa-list')


class EsposaUpdateView(UpdateView):
	model = Esposa
	success_url =  reverse_lazy('esposa-list')

class EsposaDeleteView(DeleteView):
	model = Esposa
	success_url = reverse_lazy('esposa-list')


#FILHO
class FilhoListView(ListView):
	model = Filho


class FilhoDetailView(DetailView):
	model = Filho


class FilhoCreateView(CreateView):
	model = Filho
	success_url = reverse_lazy('filho-list')


class FilhoUpdateView(UpdateView):
	model = Filho
	success_url = reverse_lazy('filho-list')
	

class FilhoDeleteView(DeleteView):
	model = Filho
	success_url = reverse_lazy('filho-list')


#Igreja
class IgrejaListView (ListView):
	model = Igreja


class IgrejaDetailView(DetailView):
	model = Igreja


class IgrejaCreateView(CreateView):
	model = Igreja
	success_url = reverse_lazy ('igreja')


class IgrejaUpdateView(UpdateView):
	model = Igreja
	success_url = reverse_lazy	


class IgrejaDeleteView(DeleteView):
	model = Igreja
	success_url = reverse_lazy		



#Carro

class CarroListView(ListView):
	model = Carro


class CarroDetailView(DetailView):
	model = Carro


class CarroCreateView(CreateView):
	model = Carro
	success_url = reverse_lazy('carro-list')


class CarroUpdateView(UpdateView):
	model = Carro
	success_url = reverse_lazy('carro-list')
		
	
class CarroDeleteView(DeleteView):
	model = Carro
	success_url = reverse_lazy('carro-list')










