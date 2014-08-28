from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Comune(models.Model):
    nome = models.CharField(max_length=255)
    codice_catastale = models.CharField(max_length=4, unique=True)

    class Meta:
        verbose_name = 'comune'
        verbose_name_plural = 'comuni'

    def __str__(self):
        return "%s: %s" % (self.codice_catastale, self.nome)
