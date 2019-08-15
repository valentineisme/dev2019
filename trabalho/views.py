from django.shortcuts import render
from trabalho import forms, models


def index(request):
    return render(request,'index.html')

def cadastro(request):
    if request.POST.get('cadastrando'):
        form = forms.UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
        return render(request, 'index.html', {'form': form})

    else:
        form = forms.UsuarioForm()
        return render(request, 'cadastro.html', {'form': form})