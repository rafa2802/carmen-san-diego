from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views as jogo

app_name = 'jogo'

urlpatterns = [
	path('', jogo.Home.as_view(), name='home'),
	path('partida/', jogo.NovaPartida.as_view(), name = 'partida'),
	path('pais/<pk>', jogo.Partida.as_view(), name = 'pais'),
	path('salvar/<pk>', jogo.SalvarPartida.as_view(), name = 'salvar'),
	path('finalizar/', jogo.Finalizar.as_view(), name = 'finalizar'),
	path('continuar/', jogo.Continuar.as_view(), name = 'continuar')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)