from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Module(models.Model):
    num = models.IntegerField(verbose_name='порядковый номер')
    title = models.CharField(max_length=100, verbose_name='название модуля')
    description = models.TextField(verbose_name='описание модуля', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'модуль'
        verbose_name_plural = 'модули'
