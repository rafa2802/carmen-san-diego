from django.urls import include, path
from django.conf.urls import include, url

from . import views as jogo

app_name = 'jogo'

urlpatterns = [
	path('', jogo.France.as_view(), name='france'),
]