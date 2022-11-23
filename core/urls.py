from django.urls import path
from .views import home, produto, servico, cadastrar_produto, cadastrar_servico, modificar_produto, eliminar_produto, eliminar_servico, modificar_servico

urlpatterns = [
    path('',home,name='home'),
    path('produto/', produto, name='produto'),
    path('cadastrar_produto', cadastrar_produto, name='cadastrar_produto'),
    path('modificar_produto/<id>', modificar_produto, name ='modificar_produto'),
    path('eliminar_produto/<id>', eliminar_produto, name='eliminar_produto'),
    path('servico/', servico, name='servico'),
    path('cadastrar_servico', cadastrar_servico, name='cadastrar_servico'),
    path('modificar_servico/<id>', modificar_servico, name ='modificar_servico'),
    path('eliminar_servico/<id>', eliminar_servico, name='eliminar_servico'),

]
