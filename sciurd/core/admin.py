from django.contrib import admin
from core.models import Pastor, Esposa, Filho, Igreja, Carro


class PatorAdmin(admin.ModelAdmin):
	list_display = ['nome', 'cpf']
	search_fields = ['nome', 'cpf']
	

class EsposaAdmin(admin.ModelAdmin):
	list_display = ('name', 'cpf')


class FilhoAdmin(admin.ModelAdmin):
	list_display  = ('nome')

class IngrejaAdmin(admin.ModelAdmin):
	list_display = ('regiao', 'pastor_regional')
	search_fields  =('regiao', 'pastor_regional')

class CarroAdmin(admin.ModelAdmin):
	list_display = ('placa', 'renavan')
	search_fields = ('placa', 'renavan')



	admin.site.register(Pastor)
	admin.site.register(Esposa)
	admin.site.register(Filho)
	admin.site.register(Igreja) 
	admin.site.register(Carro)
#admin.site.register(Carro, Carro




