from django import forms
from model import Pastor, Esposa, Filho, Igreja, Carro

class PastorForm(forms.ModelForm):

	mome = forms.CharField(label='Nome', max_length=100)
	estado_civil = forms.CharField(label='estodo_civil',max_length=20, choices = ESTADO_CIVIL_CHOICE)
	pastor_regional = forms.BooleanField(label=required=False)
	data_de_nascimento = forms.DateField(label='datetime.date.today')
	cpf = forms.CharField(label=max_length=20, blank=True)
	rg = forms.CharField(label=max_length=20)
	data_de_exp = forms.DateField(label='Data_de_Exp')
	cnh = forms.CharField(label='Cnh'max_length=20)
	regiao = forms.CharField(label='regiao'max_length=10,  choices = REGIAO_CHOICE)
	titulo_Eleitor = forms.CharField(label='Titulo_Eleitor' max_length=20)
	zona = forms.CharField(label='Zona'=max_length=10)
	seção = forms.CharField(label='Seção'max_length=20)
	passaporte = forms.CharField(label='Passaporte'max_length=15)
	nacionalidade = forms.CharField(label='Nascionalidade'max_length=20, blank=True)
	naturalidada_UF = forms.CharField(label='Naturalidade' max_length=20, blank=True)
	grau_de_Instrução = forms.CharField(label= max_length=30, choices = GRAU_DE_INSTRUÇÃO_CHOICE, blank=True)
	proficao = forms.CharField(label='Proficao'max_length=20, blank=True)
	esposa = forms.ForeignKey(label='Esposa')
	indioma = forms.CharField(label='Indioma'max_length=10)
	telefone = forms.CharField(label='Telefone'max_length=10)
	celula = forms.CharField(label='Celula'max_length=20, default= "")
	email = forms.EmailField(label='E-mail'unique=True)
	#Skayp = forms.CharField(max_length=10, blank=True)
	#Facebook = forms.CharField(max_length=20, blank=True)
	Whatsapp = forms.CharField(label= max_length=10, blank=True)
	Pastor = forms.CharField(label= 'Pastor'max_length=20,  choices = PASTOR_CHOICE, blank=True)
	#Tempo_de_Evangelho = forms.CharField(max_
		class Meta:
			model = Pastor

class EsposaForm(forms.ModelForm):

		class Meta:
			model = Esposa

class FilhoForm(forms.ModelForm):

		class Meta:
			model = Filho

class IgrejaForm(forms.ModelForm):

		class Meta:
			model = Igreja

class CarroForm(forms.ModelForm):

		class Meta:
			model = Carro

