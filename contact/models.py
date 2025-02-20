from django.db import models
from django.utils import timezone

# Criando o Modelo de Contato do Site
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=14) 
    email = models.EmailField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=500)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')

    # Identificação por nome na pagina ADMIN
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

    