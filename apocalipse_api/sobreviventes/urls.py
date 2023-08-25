from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodosSobreviventesView.as_view(), name='sobreviventes'),
    path('<int:id_sobrevivente>/', views.SobreviventeView.as_view(), name='sobrevivente'),
    path('<int:id_sobrevivente>/inventario/', views.SobreviventeInventario.as_view(), name='inventario'),
    path('<int:id_sobrevivente>/localizacao/', views.SobreviventeLocalizacao.as_view(), name='localizacao'),
    path('infectado/', views.SobreviventeInfectado.as_view(), name='infectado'),
    path('troca/', view=views.TrocaItens.as_view(), name='troca'),
]