from django import forms
from .models import Produto, Servico

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'


