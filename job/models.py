from django.db import models
from django.contrib.auth.models import User

class Referencias(models.Model):
    arquivo = models.FileField(upload_to='referencias')
    
    def __str__(self):
        return self.arquivo.url
    

class Jobs(models.Model):
    categoria_choises = (
        ('D', 'Design'),
        ('EV', 'Edição de Vídeo')
    )
    
    status_choice = (
        ('AA', 'Aguardando aprovação'),
        ('C', 'Em criação'),
        ('F', 'Finalizado')
    )
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.CharField(max_length=2, choices=categoria_choises, default='D')
    prazo_entrega = models.DateTimeField()
    preco = models.FloatField()
    referencias = models.ManyToManyField(Referencias)
    profissional = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    reservado = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=status_choice, default='AA')
    
    def __str__(self):
        return self.titulo