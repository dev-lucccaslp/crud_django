from django.shortcuts import render
from .models import Produto, Servico
from .forms import ProdutoForm, ServicoForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def home(request):
    return render(request,'home.html')


def produto(request):
    produto = Produto.objects.all()
    dados = {
        'produto': produto,
    }
    return render(request,'produto.html', dados)


def cadastrar_produto(request):
    dados = {
        'cadproduto':ProdutoForm(),
    
    }
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'cadastrar_produto.html', dados)

def modificar_produto(request, id):

    produto = get_object_or_404(Produto, id=id)

    data = {
        'form': ProdutoForm(instance=produto)
    }

    if request.method == 'POST':
        formulario = ProdutoForm(data=request.POST, instance=produto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="produto")
        data["form"] = formulario
    return render(request, 'modificar_produto.html',data)

def eliminar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect(to="produto")

def servico(request):
    servico = Servico.objects.all()
    data = {
        'servico': servico,
    }
    return render(request,'servico.html', data)

def cadastrar_servico(request):
    dados = {
        'cadservico':ServicoForm(),
    
    }
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'cadastrar_servico.html', dados)

def modificar_servico(request, id):

    servico = get_object_or_404(Servico, id=id)

    data = {
        'form': ServicoForm(instance=servico)
    }

    if request.method == 'POST':
        formulario = ServicoForm(data=request.POST, instance=servico)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="servico")
        data["form"] = formulario
    return render(request, 'modificar_servico.html',data)

def eliminar_servico(request, id):
    servico = get_object_or_404(Servico, id=id)
    servico.delete()
    return redirect(to="servico")    

