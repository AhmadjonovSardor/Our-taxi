from django.db import models
from django.utils.translation import gettext_lazy as _

class CarDeliveryType(models.Model):
    name = models.CharField(default='Kichik',choices=[
        ('Kichik','Kichik yuk'),
        ('Orta','Orta yuk'),
        ('Katta','Katta yuk'),
    ])

    def __str__(self):
        return self.name


class CarDelivery(models.Model):
    name = models.CharField(verbose_name=_('Yuk mashina turi'),max_length=32)
    height = models.PositiveSmallIntegerField(verbose_name=_('Yuk mashina balandligi'))
    width = models.PositiveSmallIntegerField(verbose_name=_('Yuk mashina eni'))
    length = models.PositiveSmallIntegerField(verbose_name=_('Yuk mashina uzunligi'))
    max_weight = models.PositiveSmallIntegerField(verbose_name=_('Qancha yuk kotara oladi?'))
    number = models.CharField(verbose_name=_('Yuk mashina raqami'), max_length=10)
    price_km = models.PositiveSmallIntegerField(verbose_name='1 km uchun narx')
    created = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(CarDeliveryType, on_delete=models.CASCADE, related_name='carDelivery_type')


    def __str__(self):
        return self.name



class CarTaxiType(models.Model):
    name = models.CharField(default='Ekanom',choices=[
        ('Ekanom','Ekanom'),
        ('Komfort','Komfort'),
        ('Lux','Lux'),
    ])

    def __str__(self):
        return self.name


class CarTaxi(models.Model):
    name = models.CharField(verbose_name='Mashina nomi',max_length=32)
    number = models.CharField(verbose_name='Mashina raqami',max_length=10)
    date = models.DateTimeField(verbose_name='Mashina bazaga qoshilgan vaqt',auto_now_add=True)
    type = models.ForeignKey(CarTaxiType,on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

class CarCargo(models.Model):
    name = models.CharField(verbose_name=_('Yuk mashina turi'),max_length=32)
    height = models.FloatField(verbose_name=_('Yuk mashina balandligi'))
    width = models.FloatField(verbose_name=_('Yuk mashina eni'))
    length = models.FloatField(verbose_name=_('Yuk mashina uzunligi'))
    max_weight = models.FloatField(verbose_name=_('Qancha yuk kotara oladi?'))
    number = models.CharField(verbose_name=_('Yuk mashina raqami'), max_length=10)
    price_km = models.PositiveSmallIntegerField(verbose_name='1 km uchun narx')
    created = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(CarDeliveryType, on_delete=models.CASCADE,)


    def __str__(self):
        return self.name
