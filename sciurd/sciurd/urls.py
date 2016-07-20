from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import *

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name= 'home'),
    
    #url(r'^cadastro/$', CadastroView.as_view(), name= 'cadastro'),
           
    url(r'^pastor/$', PastorListView.as_view(), name= 'pastor-list'),
    url(r'^pastor/(?P<pk>\d+)$', PastorDetailView.as_view(), name= 'pastor-detail'),
    url(r'^pastor/add/$', PastorCreateView.as_view(), name= 'pastor-add'),
    url(r'^pastor/editar/(?P<pk>\d+)$', PastorUpdateView.as_view(), name= 'pastor-edit'),
    url(r'^pastor/deletar/(?P<pk>\d+)$', PastorDeleteView.as_view(), name= 'pastor-delete'),

    url(r'^esposa/$', EsposaListView.as_view(), name= 'esposa-list'),
    url(r'^esposa/(?P<pk>\d+)$', EsposaDetailView.as_view(), name= 'esposa-detail'),
    url(r'^esposa/add/$', EsposaCreateView.as_view(), name= 'esposa-add'),
    url(r'^esposa/editar/(?P<pk>\d+)$', EsposaUpdateView.as_view(), name= 'esposa-edit'),
    url(r'^esposa/deletar/(?P<pk>\d+)$', EsposaDeleteView.as_view(), name= 'esposa-delete'),

    url(r'^filho/$', FilhoListView.as_view(), name= 'filho-list'),
    url(r'^filho/(?P<pk>\d+)$', FilhoDetailView.as_view(), name= 'filho-detail'),
    url(r'^filho/add/$', FilhoCreateView.as_view(), name= 'filho-add'),
    url(r'^fihlo/editar/(?P<pk>\d+)$', FilhoUpdateView.as_view(), name= 'filho-edit'),
    url(r'^filho/deletar/(?P<pk>\d+)$', FilhoDeleteView.as_view(), name= 'filho-delete'),

    url(r'^igreja/$', IgrejaListView.as_view(), name= 'igreja-list'),
    url(r'^igreja/(?P<pk>\d+)$', IgrejaDetailView.as_view(), name= 'igreja-detail'),
    url(r'^igreja/add/$', IgrejaCreateView.as_view(), name= 'igreja-add'),
    url(r'^igreja/editar/(?P<pk>\d+)$', IgrejaUpdateView.as_view(), name= 'igreja-edit'),
    url(r'^igreja/deletar/(?P<pk>\d+)$', IgrejaDeleteView.as_view(), name= 'igreja-delete'),

    url(r'^carro/$', CarroListView.as_view(), name= 'carro-list'),
    url(r'^carro/(?P<pk>\d+)$', CarroDetailView.as_view(), name= 'carro-Detail'),
    url(r'^carro/add/$', CarroCreateView.as_view(), name= 'carro-add'),
    url(r'^carro/editar/(?P<pk>\d+)$', CarroUpdateView.as_view(), name= 'carro-edit'),
    url(r'^carro/delete/(?P<pk>\d+)$', CarroDeleteView.as_view(), name= 'carro-delete'),

    #sgpiurd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)