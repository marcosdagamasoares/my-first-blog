from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model): # esta linha define o nosso modelo (é um objeto).
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               verbose_name='Autor')
    title = models.CharField(max_length=200, verbose_name='Título')
    text = models.TextField(verbose_name='Texto')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Data Criação')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Data Publicação')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # quando chamarmos __str__(), obteremos um texto (string) com o título do Post.
        return self.title
