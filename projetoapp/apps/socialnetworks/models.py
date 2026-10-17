from django.db import models

# Create your models here.

class SocialNetwork(models.Model):
    name = models.CharField('Nome', max_length=50)
    content_type = models.CharField('Tipo de Conteudo', max_length=100)
    url = models.CharField('URL', max_length=200)

    class Meta:
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'
        ordering =['id']

    def __str__(self):
        return f'{self.name}'
