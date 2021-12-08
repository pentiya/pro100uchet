from django.db import models

# Create your models here.

class Ivc(models.Model):
    name = models.CharField('Имя', max_length = 50)
    short_name = models.CharField('краткое имя', max_length = 10)

    class Meta:
        ordering = ('name',)
        verbose_name = 'ИВЦ'
        verbose_name_plural = 'ИВЦ'

    def __str__ (self):
        return self.name

class Rivc(models.Model):
    name = models.CharField('РИВЦ', max_length = 50)
    kod = models.IntegerField('Код',default=0)
    ivc = models.ForeignKey('Ivc', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'РИВЦ'
        verbose_name_plural = 'РИВЦ'

    def __str__ (self):
        return self.name


class Usel(models.Model):
    name = models.CharField('Имя узла', max_length = 100)
    ivc = models.ForeignKey('Ivc', on_delete=models.CASCADE)
    rivc = models.ForeignKey('Rivc', on_delete=models.CASCADE)
    station = models.ForeignKey('rzd.Station', on_delete=models.CASCADE)
#   date = models.DateTimeField('дата изменения')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Узел'
        verbose_name_plural = 'Узлы'

    def __str__ (self):
        return self.name

'''
class UselType(models.Model):
    USEL_TYPE = [
        ('ОУ', 'ОУ'),
        ('ПУ', 'ПУ'),
        ('ТПУ', 'ТПУ'),
        ('РУ', 'РУ'),
    ]
    name = models.CharField('тип узла', max_length = 3,
        choices=USEL_TYPE, default='ОУ',
        )
#   date = models.DateTimeField('дата изменения')

    def __str__ (self):
        return self.name
        verbose_name = 'Тип узла'
        verbose_name_plural = 'Типы узлов' 
'''
