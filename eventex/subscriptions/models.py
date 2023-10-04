import uuid

from django.db import models


# Create your models here.
class Subscription(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefone', max_length=20)
    created_at = models.DateTimeField('Criado em', auto_now=True)

    class Meta:
        verbose_name_plural = 'Inscrições'
        verbose_name = 'Inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name