from django.db import models
from app.core.models import UUIDUser

class Pais(models.Model):
	nome = models.CharField(max_length = 75, verbose_name = 'Nome do País')
	descricao = models.TextField(verbose_name = 'Descrição')
	imagem_pais = models.ImageField(upload_to='paises/', verbose_name = 'Imagem do País')
	testemunha_um_nome = models.CharField(max_length = 75, verbose_name = 'Nome da Testemunha Um')
	testemunha_um_fala = models.TextField(verbose_name = 'Fala da Testemunha Um')
	testemunha_um_imagem = models.ImageField(upload_to='testemunhas/', verbose_name = 'Imagem da Testemunha Um')
	testemunha_dois_nome = models.CharField(max_length = 75, verbose_name = 'Nome da Testemunha Dois')
	testemunha_dois_fala = models.TextField(verbose_name = 'Fala da Testemunha Dois')
	testemunha_dois_imagem = models.ImageField(upload_to='testemunhas/', verbose_name = 'Imagem da Testemunha Dois')
	pais_um = models.ForeignKey('Pais', on_delete = models.CASCADE, related_name = 'paisum', verbose_name = 'País Um', blank = True, null = True)
	pais_um_imagem = models.ImageField(upload_to='paises/', verbose_name = 'Bandeira do País Um', blank = True, null = True)
	pais_dois = models.ForeignKey('Pais', on_delete = models.CASCADE, related_name = 'paisdois', verbose_name = 'País Dois', blank = True, null = True)
	pais_dois_imagem = models.ImageField(upload_to='paises/', verbose_name = 'Bandeira do País Dois', blank = True, null = True)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'País'
		verbose_name_plural = 'Paises'

class Save(models.Model):
	usuario = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'user', verbose_name = 'Usuário')
	pais = models.ForeignKey(Pais, on_delete = models.CASCADE, related_name = 'pais', verbose_name = 'País')
	criado_em = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return 'Salvamento da partida do Usuário: %s' % self.usuario.username

	class Meta:
		ordering = ["criado_em"]
		verbose_name = 'Salvamento'
		verbose_name_plural = 'Salvamentos'
