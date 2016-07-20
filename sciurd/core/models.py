from django.db import models


class Pastor(models.Model):

	REGIAO_CHOICE = (
		('barao',  'BARAO'),
		('lorival', 'LORIVAL'),
		('sede', 's')
	)

	ESTADO_CIVIL_CHOICE = (
		('C', 'CASADO'),
		('D', 'DIRVOCIADO'),
		('S', 'SOLTEIRO'),
		('V', 'VIUVO')
	)
	
	GRAU_DE_INSTRUÇÃO_CHOICE = (
		('1°', '1°Grau'),
		('2°', '2°Grau'),
		('S', 'Superior'),
	)
	
	PASTOR_CHOICE = (
		('Aux', 'Auxiliar'),
		('Pr', 'Pr.Titular'),
		('Bp', ' Bispo'),
	)
	

	Nome = models.CharField('Nome', max_length=30)
	estado_civil = models.CharField(max_length=10, choices = ESTADO_CIVIL_CHOICE)
	Pastor_Regional = models.BooleanField(default=False)
	Data_de_Nascimento = models.DateField('Data_de_Nascimento')
	Cpf = models.CharField('Cpf', max_length=20, blank=True)
	Rg = models.CharField(max_length=20)
	Data_de_Exp = models.DateField('Data_de_Exp')
	Cnh = models.CharField(max_length=20)
	Regiao = models.CharField(max_length=10,  choices = REGIAO_CHOICE)
	Titulo_Eleitor = models.CharField(max_length=20)
	Zona = models.CharField(max_length=10)
	Seção = models.CharField(max_length=20)
	Passaporte = models.CharField(max_length=15)
	Nacionalidade = models.CharField(max_length=20, blank=True)
	Naturalidada_UF = models.CharField(max_length=20, blank=True)
	Grau_de_Instrução = models.CharField(max_length=30, choices = GRAU_DE_INSTRUÇÃO_CHOICE, blank=True)
	Proficao = models.CharField(max_length=20, blank=True)
	Esposa = models.ForeignKey('Esposa',)
	Indioma = models.CharField(max_length=10)
	Telefone = models.CharField(max_length=10)
	Celula = models.CharField(max_length=20, default= "")
	Email = models.EmailField(unique=True)
	#Skayp = models.CharField(max_length=10, blank=True)
	#Facebook = models.CharField(max_length=20, blank=True)
	Whatsapp = models.CharField(max_length=10, blank=True)
	Pastor = models.CharField(max_length=20,  choices = PASTOR_CHOICE, blank=True)
	#Tempo_de_Evangelho = models.CharField(max_length=15, blank=True)

	class Meta:
		verbose_name = ('Pastor')
		verbose_name_plural = ('Pastores')


	def __unicode__(self):
		return self.Nome
		verbose_name = 'Pastor'
		verbose_name_plural = 'Pastor'


class Esposa(models.Model):

	Nome = models.CharField(max_length=20)
	Casamento_Data = models.DateField('Certidao_de_Casamento')
	Cpf = models.CharField('CPF', max_length=11, unique=True)
	Rg = models.CharField(max_length=20)
	Data_de_Exp = models.DateField('Data_de_Exp')
	Titulo_Eleitor = models.CharField(max_length=20)
	Passaporte = models.CharField(max_length=20, blank=True)
	Nacionalidade = models.CharField(max_length=20, blank=True)
	Naturalidade = models.CharField(max_length=20, blank=True)
	Formacao = models.CharField(max_length=20, blank=True)
	Proficao = models.CharField(max_length=20)
	Indioma = models.CharField(max_length=10, blank=True)
	Tempo_de_Evangelho = models.CharField(max_length=10, blank=True)

	class Meta:
		verbose_name = ('Esposa')
		verbose_name_plural = ('Esposas')

	def __unicode__(self):
		return self.Nome
		verbose_name = 'Esposa'
		verbose_name = 'Esposas'


class Filho(models.Model):
	Nome = models.CharField(max_length=30)
	Data_de_Nascimento = models.DateField('Data_de_Nascimento')

	class Meta:
		verbose_name = ('Filho')
		verbose_name_plural = ('Filhos')

	def __unicode__(self):
		return self.Nome
		verbose_name = 'Esposa'
		verbose_name = 'Esposas'


	

class Igreja(models.Model):


	IURD_CHOICE = (
		('barao',  'BARAO'),
		('lorival', 'LORIVAL'),
		('sede', 's')
	)


	IURD = models.CharField(max_length=10, choices = IURD_CHOICE, blank=True)
	CNPJ =models.CharField(max_length=15, blank=True)
	Contato =models.CharField(max_length=15, blank=True)
	Endereco =models.CharField(max_length=15, blank=True)
	Numero =models.CharField(max_length=15)
	Bairro  =models.CharField(max_length=15, blank=True)
	Cidade  =models.CharField(max_length=15, blank=True)
	Cep =models.CharField(max_length=15, blank=True)
	Telefone =models.CharField(max_length=15, blank=True)
	Email = models.CharField(max_length=15, blank=True)
	#Pastores_da_Regiao = models.CharField(max_length=20)
	Possui_Carro = models.BooleanField(default=True)
	Carro = models.ForeignKey('Carro')
	

	class Meta:
		verbose_name = ('Igreja')
		verbose_name_plural = ('Igrejas')

	def __unicode__(self):
		return self.Nome
		verbose_name = 'Esposa'
		verbose_name = 'Esposas'


#Carro
class Carro(models.Model):
	Placa = models.CharField(max_length=20, default = 'xxx-xxxx')
	Renava = models.CharField(max_length=20)
	Marca = models.CharField(max_length=20)
	Modelo = models.CharField(max_length=20)
	Ano = models.IntegerField()

	class Meta:
		verbose_name = ('Carro')
		verbose_name_plural = ('Carros')

	def __unicode__(self):
		return self.Placa
		verbose_name = 'Carro'
		verbose_name = 'Carros'

