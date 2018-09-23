from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views import View

from django.urls import reverse_lazy
from .models import Pais, Save

class Home(View):
	def get(self, request):
		return render(request, 'jogo/start.html')

class NovaPartida(View):
	def get(self, request):
		pais = Pais.objects.filter(nome = 'Paris - França').first()
		print (pais.pk)
		return render(request, 'jogo/game.html', {'pais': pais})

class Partida(View):
	def get(self, request, pk):
		pais = Pais.objects.filter(id = pk).first()
		if pk == "6":
			return render(request, 'jogo/fim.html', {'pais': pais})	
		return render(request, 'jogo/game.html', {'pais': pais})

class SalvarPartida(View):
	def get(self, request, pk):
		pais = Pais.objects.filter(id = pk).first()
		salvar = Save(usuario = self.request.user, pais = pais)
		salvar.save()
		return redirect('jogo:home')

class Finalizar(View):
	def get(self, request):
		salvamentos = Save.objects.filter(usuario = self.request.user)
		for salvar in salvamentos:
			salvar.delete()
		return redirect('jogo:home')

class Continuar(View):
	def get(self, request):
		salvamentos = Save.objects.filter(usuario = self.request.user).order_by('-criado_em')
		if len(salvamentos) == 0:
			return render(request, 'jogo/start.html', {'mensagem': 'Desculpe, você não salvou nenhuma partida!'})
		else:
			return render(request, 'jogo/game.html', {'pais': salvamentos[0].pais})


