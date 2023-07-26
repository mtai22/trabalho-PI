from django.contrib import admin
from .models import Descricao, Categoria
# Register your models here.
@admin.register(Descricao)
class DescricaoAdmin(admin.ModelAdmin):
    list_display=('quant_folhas','quant_materias','marca','tamanho','design', 'tipo')
  
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=( 'tipo',)  

    

    