from django.db import models


class Pastor(models.Model):

    REGIAO_CHOICE = (
        ('barao', 'BARAO'),
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

    nome = models.CharField('Nome', max_length=30)
    estado_civil = models.CharField(
        max_length=10, choices=ESTADO_CIVIL_CHOICE
    )
    pastor_regional = models.BooleanField(default=False)
    data_de_nascimento = models.DateField('Data_de_Nascimento')
    cpf = models.CharField('Cpf', max_length=20, blank=True)
    rg = models.CharField(max_length=20)
    data_de_exp = models.DateField('Data_de_Exp')
    cnh = models.CharField(max_length=20)
    regiao = models.CharField(max_length=10, choices=REGIAO_CHOICE)
    titulo_eleitor = models.CharField(max_length=20)
    zona = models.CharField(max_length=10)
    seção = models.CharField(max_length=20)
    passaporte = models.CharField(max_length=15)
    nacionalidade = models.CharField(max_length=20, blank=True)
    naturalidada_uf = models.CharField(max_length=20, blank=True)
    grau_de_instrução = models.CharField(
        max_length=30,
        choices=GRAU_DE_INSTRUÇÃO_CHOICE,
        blank=True
    )
    proficao = models.CharField(max_length=20, blank=True)
    esposa = models.ForeignKey('Esposa',)
    indioma = models.CharField(max_length=10)
    telefone = models.CharField(max_length=10)
    celula = models.CharField(max_length=20, default="")
    email = models.EmailField(unique=True)
    # Skayp = models.CharField(max_length=10, blank=True)
    # Facebook = models.CharField(max_length=20, blank=True)
    whatsapp = models.CharField(max_length=10, blank=True)
    pastor = models.CharField(
        max_length=20,
        choices=PASTOR_CHOICE,
        blank=True
    )
    # Tempo_de_Evangelho = models.CharField(max_length=15, blank=True)

    class Meta:
        verbose_name = 'Pastor'
        verbose_name_plural = 'Pastores'

    def __unicode__(self):
        return self.Nome


class Esposa(models.Model):

    nome = models.CharField(max_length=20)
    casamento_data = models.DateField('Certidao_de_Casamento')
    cpf = models.CharField('CPF', max_length=11, unique=True)
    rg = models.CharField(max_length=20)
    data_de_exp = models.DateField('Data_de_Exp')
    titulo_eleitor = models.CharField(max_length=20)
    passaporte = models.CharField(max_length=20, blank=True)
    nacionalidade = models.CharField(max_length=20, blank=True)
    naturalidade = models.CharField(max_length=20, blank=True)
    formacao = models.CharField(max_length=20, blank=True)
    proficao = models.CharField(max_length=20)
    indioma = models.CharField(max_length=10, blank=True)
    tempo_de_evangelho = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name = 'Esposa'
        verbose_name_plural = 'Esposas'

    def __unicode__(self):
        return self.Nome


class Filho(models.Model):
    nome = models.CharField(max_length=30)
    data_de_nascimento = models.DateField('Data_de_Nascimento')

    class Meta:
        verbose_name = 'Filho'
        verbose_name_plural = 'Filhos'

    def __unicode__(self):
        return self.Nome


class Igreja(models.Model):

    IURD_CHOICE = (
        ('barao', 'BARAO'),
        ('lorival', 'LORIVAL'),
        ('sede', 's')
    )

    IURD = models.CharField(
        max_length=10,
        choices=IURD_CHOICE,
        blank=True
    )
    bairro = models.CharField(max_length=15, blank=True)
    carro = models.ForeignKey('Carro')
    cep = models.CharField(max_length=15, blank=True)
    cidade = models.CharField(max_length=15, blank=True)
    cnpj = models.CharField(max_length=15, blank=True)
    contato = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=15, blank=True)
    endereco = models.CharField(max_length=15, blank=True)
    numero = models.CharField(max_length=15)
    possui_carro = models.BooleanField(default=True)
    telefone = models.CharField(max_length=15, blank=True)
    # Pastores_da_Regiao = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Igreja'
        verbose_name_plural = 'Igrejas'

    def __unicode__(self):
        return self.Nome


class Carro(models.Model):
    placa = models.CharField(max_length=20, default='xxx-xxxx')
    renavan = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    ano = models.IntegerField()

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __unicode__(self):
        return self.Placa
