from django.db import models

class Categoria(models.Model):
    tipo = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.tipo


class Descricao(models.Model):
    quant_folhas = models.IntegerField()
    quant_materias = models.IntegerField()
    marca = models.CharField(max_length=150) 
    tamanho = models.CharField(max_length=100)
    design = models.CharField(max_length=150)
    tipo = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="imagem")