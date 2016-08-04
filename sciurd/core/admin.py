from django.contrib import admin
from core.models import Pastor, Esposa, Filho, Igreja, Carro


class PastorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf']
    search_fields = ['nome', 'cpf']


class EsposaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')


class FilhoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class IgrejaAdmin(admin.ModelAdmin):
    list_display = ('IURD', 'endereco')
    search_fields = ('IURD', 'endereco')


class CarroAdmin(admin.ModelAdmin):
    list_display = ('placa', 'renavan')
    search_fields = ('placa', 'renavan')


admin.site.register(Pastor, PastorAdmin)
admin.site.register(Esposa, EsposaAdmin)
admin.site.register(Filho, FilhoAdmin)
admin.site.register(Igreja, IgrejaAdmin)
admin.site.register(Carro, CarroAdmin)
# admin.site.register(Carro, Carro
