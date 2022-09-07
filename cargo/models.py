from django.db import models


class Weight(models.Model):
    title = models.CharField(max_length=100, verbose_name='Вес')
    kilo = models.IntegerField(blank=False, verbose_name='Широта')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Вес'
        verbose_name_plural = 'Вес'
        ordering = ['id']



class Price(models.Model):
    title = models.CharField(max_length=100, verbose_name='Сумма')
    money = models.IntegerField(blank=False, verbose_name='Широта')
    kilo = models.OneToOneField('Weight', on_delete=models.CASCADE, null=True)
    km = models.ForeignKey('Distance', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Сумма'
        verbose_name_plural = 'Сумма'
        ordering = ['id']


class Distance(models.Model):
    title = models.CharField(max_length=100, verbose_name='Координаты')
    longitude_1 = models.IntegerField(blank=False, verbose_name='Долгота_1')
    longitude_2 = models.IntegerField(blank=False, verbose_name='Долгота_2')
    latitude_1 = models.IntegerField(blank=False, verbose_name='Широта_1')
    latitude_2 = models.IntegerField(blank=False, verbose_name='Широта_2')
    mone = models.ForeignKey('Price', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Расстояние'
        verbose_name_plural = 'Расстояние'
        ordering = ['id']