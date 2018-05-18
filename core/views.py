from django.shortcuts import render, redirect
from core.forms import *

#AUX - slug
def slug_cliente(nome, cpf, uf):
    nomeAux = nome.split(" ")
    cpfAux = cpf.split('.')
    cpf = '{}{}{}'.format(cpfAux[0], cpfAux[1], cpfAux[2])
    return "{}-{}-{}".format(nomeAux[0], cpf, uf)

def slug_fornecedor(nome, cnpj):
    nomeAux = nome.split(" ")
    cnpj = '{}{}{}{}{}{}'.format(cnpj[0], cnpj[1], cnpj[2], cnpj[3], cnpj[4], cnpj[5])
    return '{}{}'.format(nomeAux[0], cnpj)

# Create your views here.
def home(request):
    return render(request, "index.html")

def cadastro_cliente(request):
    if request.POST:
        form = ClienteForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.slug = slug_cliente(forms.nome_contato, forms.cpf_cnpj, forms.estado)
            forms.save()
            return redirect('/cadastro_cliente')
    else:
        form = ClienteForm()

    context = {
        'form': form
    }

    return render(request, "cadastro_clientes.html", context)

def clientes(request):
    clientes = Cliente.objects.all()

    context = {
        'clientes': clientes
    }

    return render(request, "clientes.html", context)

def cliente(request, slug):
    cliente = Cliente.objects.get(slug=slug)

    context = {
        'cliente': cliente
    }

    return render(request, "detalhes_cliente.html", context)

def cadastro_orcamento(request):
    if request.POST:
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cadastro_orcamento')
    else:
        form = OrcamentoForm()

    context = {
        'form': form
    }
    return render(request, "cadastro_orcamento.html", context)

def cadastro_fornecedor(request):
    slug = ''
    if request.POST:
        form = FornecedorForm(request.POST)
        formM = FornecedorMaterialForm(request.POST)
        if form.is_valid() and formM.is_valid():
            forms = form.save(commit=False)
            forms.slug = slug_fornecedor(forms.nome_fantasia, forms.cnpj)
            slug = forms.slug
            forms.save()
            formsM = formM.save(commit=False)
            fornecedor = Fornecedor.objects.get(slug=slug)
            formsM.id_fornecedor = fornecedor
            formsM.save()
            return redirect('/cadastro_fornecedor')
    else:
        form = FornecedorForm()
        formM = FornecedorMaterialForm()

    context = {
        'form': form,
        'formM': formM
    }

    return render(request, "cadastro_fornecedor.html", context)

def fornecedores(request):
    fornecedores = Fornecedor.objects.all()

    context = {
        'fornecedores': fornecedores
    }

    return render(request, 'fornecedores.html', context)

def estoque_cadastrarMateriais(request):
    if request.POST:
        form = MaterialForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/estoque_cadastrarMateriais')
    else:
        form = MaterialForm()

    context = {
        'form': form
    }

    return render(request, 'estoque_cadastrarMateriais.html', context)

def estoque(request):
    return render(request, 'estoque.html')

def detalhes_fornecedor(request, slug):
    fornecedor = Fornecedor.objects.get(slug=slug)
    context = {
        'fornecedor': fornecedor
    }
    return render(request, 'detalhes_fornecedor.html', context)