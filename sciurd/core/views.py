from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.core.urlresolvers import reverse_lazy

from core.models import Pastor, Esposa, Filho, Igreja, Carro
from core.forms import (
    PastorForm,
    EsposaForm,
    FilhoForm,
    IgrejaForm,
    CarroForm,
)


class HomeView(TemplateView):
    template_name = 'index.html'


class PastorCreateView(CreateView):
    template_name = 'add.html'
    form_class = PastorForm
    model = Pastor
    success_url = reverse_lazy('pastor-add')

    def get_context_data(self, **kwargs):
        context = super(PastorCreateView, self).get_context_data(**kwargs)
        context['cadastro'] = 'Pastor'
        return context


class PastorListView(ListView):
    template_name = 'view.html'
    model = Pastor


class PastorDetailView(DetailView):
    template_name = 'detail.html'
    model = Pastor


class PastorUpdateView(UpdateView):
    template_name = 'update.html'
    model = Pastor
    success_url = '/pastor/'


class PastorDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Pastor
    success_url = reverse_lazy('pastor-list')


class EsposaCreateView(CreateView):
    form_class = EsposaForm
    template_name = 'esposa.html'
    model = Esposa
    success_url = reverse_lazy('esposa-list')

    def get_context_data(self, **kwargs):
        context = super(EsposaCreateView, self).get_context_data(**kwargs)
        context['cadastro'] = 'Esposa'
        return context


class EsposaListView(ListView):
    model = Esposa
    success_url = reverse_lazy('listar')


class EsposaDetailView(DetailView):
    model = Esposa


class EsposaUpdateView(UpdateView):
    model = Esposa
    success_url = reverse_lazy('esposa-list')


class EsposaDeleteView(DeleteView):
    model = Esposa
    success_url = reverse_lazy('esposa-list')


class FilhoListView(ListView):
    model = Filho


class FilhoDetailView(DetailView):
    model = Filho


class FilhoCreateView(CreateView):
    form_class = FilhoForm
    model = Filho
    success_url = reverse_lazy('filho-list')
    template_name = 'add.html'

    def get_context_data(self, **kwargs):
        context = super(FilhoCreateView, self).get_context_data(**kwargs)
        context['cadastro'] = 'Filho'
        return context


class FilhoUpdateView(UpdateView):
    model = Filho
    success_url = reverse_lazy('filho-list')


class FilhoDeleteView(DeleteView):
    model = Filho
    success_url = reverse_lazy('filho-list')


class IgrejaListView (ListView):
    model = Igreja


class IgrejaDetailView(DetailView):
    model = Igreja


class IgrejaCreateView(CreateView):
    form_class = IgrejaForm
    model = Igreja
    success_url = reverse_lazy('igreja-list')
    template_name = 'add.html'

    def get_context_data(self, **kwargs):
        context = super(IgrejaCreateView, self).get_context_data(**kwargs)
        context['cadastro'] = 'Igreja'
        return context


class IgrejaUpdateView(UpdateView):
    model = Igreja
    success_url = reverse_lazy


class IgrejaDeleteView(DeleteView):
    model = Igreja


class CarroListView(ListView):
    model = Carro


class CarroDetailView(DetailView):
    model = Carro


class CarroCreateView(CreateView):
    form_class = CarroForm
    model = Carro
    success_url = reverse_lazy('carro-list')
    template_name = 'add.html'

    def get_context_data(self, **kwargs):
        context = super(CarroCreateView, self).get_context_data(**kwargs)
        context['cadastro'] = 'Carro'
        return context


class CarroUpdateView(UpdateView):
    model = Carro
    success_url = reverse_lazy('carro-list')


class CarroDeleteView(DeleteView):
    model = Carro
    success_url = reverse_lazy('carro-list')
