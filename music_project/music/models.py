from django.db import models

class Banda(models.Model):
	"""docstring for Banda"""
	musicos = models.ManyToManyField(Musico)
	estilo = models.ForeignKey(EstiloMusical, on_delete=models.CASCADE)

	nome = models.TextField()
	data_de_criacao = models.DateField(auto_now = True)
	numero_de_integrantes = models.IntegerField()
	banda_choices = (
		(0,'Em atividade'),
		(1,'Banda encerrada')
	)
	em_atividade = models.IntegerField(choices = banda_choices, default = 0)
		

class Musico(models.Model):
	"""docstring for Musico"""
	nome = models.TextField()
	data_de_nascimento = models.DateField(auto_now = True)
	anos_de_carreira = models.BigIntegerField()

class EstiloMusical(models.Model):
	"""docstring for EstiloMusical"""
	nome = models.TextField()
	surgimento = models.DateField(auto_now = True)
		

		
		