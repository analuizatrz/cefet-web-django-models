from django.db import models

class Musico(models.Model):
	"""docstring for Musico"""
	nome = models.TextField()
	data_de_nascimento = models.DateField(auto_now = True)
	anos_de_carreira = models.BigIntegerField()

	def __str__(self):
		return "{nome} ({data_de_nascimento}): {anos_de_carreira} anos de carreira".format(nome = self.nome, data_de_nascimento = self.data_de_nascimento, anos_de_carreira = self.anos_de_carreira)

class EstiloMusical(models.Model):
	"""docstring for EstiloMusical"""
	nome = models.TextField()
	surgimento = models.DateField(auto_now = True)

	def __str__(self):
		return "{nome} ({surgimento})".format(nome = self.nome, surgimento = self.surgimento)
		
class Banda(models.Model):
	"""docstring for Banda"""
	musicos = models.ManyToManyField(Musico)
	estilo = models.ForeignKey(EstiloMusical, on_delete=models.CASCADE, related_name='User', null=True)

	nome = models.TextField()
	data_de_criacao = models.DateField(auto_now = True)
	numero_de_integrantes = models.IntegerField()
	banda_choices = (
		(0,'Em atividade'),
		(1,'Banda encerrada')
	)
	em_atividade = models.IntegerField(choices = banda_choices, default = 0)

	def __str__(self):
		return "{nome} \ncriada em {data_de_criacao} \nEstilo: {estilo} \nMusicos: {musicos}".format(nome=self.nome, data_de_criacao=self.data_de_criacao, estilo=self.estilo, musicos = ", ".join([m for m in self.musicos]))