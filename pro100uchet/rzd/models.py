from django.db import models

# Create your models here.

class Doroga(models.Model):
    name = models.CharField('Название дороги',max_length=255)
    kod  = models.IntegerField('Код дороги',default=0)
    short_name = models.CharField('Краткое имя дороги)',max_length=10,default='')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Дорога'
        verbose_name_plural = 'Дороги'

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField('Название региона',max_length=255,)
    kod  = models.IntegerField('Код региона',default=0)
#    doroga = models.ForeignKey('Doroga', on_delete=models.PROTECT, blank=True, null=True)
    doroga = models.ForeignKey(Doroga, on_delete=models.PROTECT)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.name


class Station(models.Model):
    name = models.CharField('Станция',max_length=255,)
    kod = models.IntegerField('Код станции',default=0)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    rvc = models.IntegerField('РВЦ',default=0)
    lon = models.FloatField('Долгота',default=0)
    lat = models.FloatField('Широта',default=0)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'

    def __str__(self):
        return self.name


class Zdanie(models.Model):
    name = models.CharField('Здание',max_length=255,)
#    kod = models.IntegerField(default=0)
    Station = models.ForeignKey(Station, on_delete=models.PROTECT)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'

    def __str__(self):
        return self.name

