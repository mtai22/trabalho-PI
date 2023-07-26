from django.shortcuts import render,get_object_or_404,redirect
from .models import Descricao
from .forms import DescricaoForm
# Create your views here.

def descricao_editar(request,id):
    descricao = get_object_or_404(Descricao,id=id)
   
    if request.method == 'POST':
        form = DescricaoForm(request.POST,instance=descricao)
        if form.is_valid():
            form.save()
            return redirect('descricao_listar')
    else:
        form = DescricaoForm(instance=descricao)

    return render(request,'descricao/form.html',{'form':form})


def descricao_remover(request, id):
    descricao = get_object_or_404(Descricao, id=id)
    descricao.delete()
    return redirect('descricao_listar') 


def descricao_criar(request):
    if request.method == 'POST':
        form = DescricaoForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('descricao_listar')
        
    form = DescricaoForm()
    return render(request, "descricao/form.html", {'form': form})


def descricao_listar(request):
    descricoes = Descricao.objects.all()
    context ={
        'descricoes':descricoes
    }
    print(descricoes)
    return render(request, "descricao/descricoes.html",context)

def index(request):
    descricoes = Descricao.objects.all()
    context ={
        'descricoes':descricoes
    }
    return render(request, 'tipo/tipo.html', context)

def detalhe(request, id):
    produto = get_object_or_404(Descricao, id=id)
    context ={
        'descricoes':produto
    }
    return render(request, 'tipo/detalhe.html', context)