from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodosSobreviventesView.as_view(), name='sobreviventes'),
    path('<uuid:id_jogo>/', views.SobreviventeIdJogoView.as_view(), name='sobreviventes_jogo'),
    path('novo_jogo/', views.CriaIdJogoView.as_view(), name='novo_jogo'),
    path('<int:id_sobrevivente>/', views.SobreviventeView.as_view(), name='sobrevivente'),
    path('<int:id_sobrevivente>/inventario/', views.SobreviventeInventario.as_view(), name='inventario'),
    path('localizacao/', views.SobreviventeLocalizacao.as_view(), name='localizacao'),
    path('infectado/', views.SobreviventeInfectado.as_view(), name='infectado'),
    path('troca/', view=views.TrocaItens.as_view(), name='troca'),
    path('<uuid:id_jogo>/nova_acao/', views.NovaAcao.as_view(), name='nova_acao'),
]