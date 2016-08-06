from django import forms
from .models import (
    Pastor,
    Esposa,
    Filho,
    Igreja,
    Carro,
)


class PastorForm(forms.ModelForm):
    # Tempo_de_Evangelho = forms.CharField(max_

    class Meta:
        model = Pastor
        fields = '__all__'


class EsposaForm(forms.ModelForm):

    class Meta:
        model = Esposa
        fields = '__all__'


class FilhoForm(forms.ModelForm):

    class Meta:
        model = Filho
        fields = '__all__'


class IgrejaForm(forms.ModelForm):

    class Meta:
        model = Igreja
        fields = '__all__'


class CarroForm(forms.ModelForm):

    class Meta:
        model = Carro
        fields = '__all__'
