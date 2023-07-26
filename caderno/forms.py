from django.forms import ModelForm
from django import forms
from .models import Descricao

class DescricaoForm(ModelForm):

    class Meta:
        model = Descricao
        fields = '__all__'
        widgets = {
            'quant_folhas' : forms.TextInput(attrs={'class': 'form-control' }),
            'quant_materias' : forms.TextInput(attrs={'class': 'form-control' }),
            'marca' : forms.TextInput(attrs={'class': 'form-control' }),
            'tamanho' : forms.TextInput(attrs={'class': 'form-control' }),
            'design' : forms.TextInput(attrs={'class': 'form-control' }),
            'tipo': forms.Select(attrs={'class': 'form-control' }), 
        }
        
       