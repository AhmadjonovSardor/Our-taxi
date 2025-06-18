from django.db import models
from django.utils.translation import gettext_lazy as _

class CarDeliveryType(models.Model):
    name = models.CharField(default=1,choices=[
        (1,'Kichik yuk'),
        (2,'Orta yuk'),
        (3,'Katta yuk'),
    ])

    def __str__(self):
        return self.name


class CarDelivery(models.Model):
    name = models.CharField(verbose_name=_('Yuk mashina turi'),max_length=32)
    height = models.PositiveSmallIntegerField(verbose_name=_('Yuk mashina balandligi'))
    width = models.PositiveSmallIntegerField(verbose_name=_('Yuk mashina eni'))
    length = models.PositiveSmallIntegerField(verbose_name=_('Yuk mashina uzunligi'))
    image = models.ImageField(verbose_name=_('Yuk mashina rasmi'),upload_to='Delivery/image/')
    max_weight = models.PositiveSmallIntegerField(verbose_name=_('Qancha yuk kotara oladi?'))
    number = models.CharField(verbose_name=_('Yuk mashina raqami'), max_length=10)
    price_km = models.PositiveSmallIntegerField(verbose_name='1 km uchun narx')
    created = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(CarDeliveryType, on_delete=models.CASCADE, related_name='carDelivery_type')


    def __str__(self):
        return self.name



class CarTaxiType(models.Model):
    name = models.CharField(default=1,choices=[
        (1,'Ekanom'),
        (2,'Komfort'),
        (3,'Lux'),
    ])

    def __str__(self):
        return self.name


class CarTaxi(models.Model):
    name = models.CharField(verbose_name='Mashina nomi',max_length=32)
    number = models.CharField(verbose_name='Mashina raqami',max_length=10)
    date = models.DateTimeField(verbose_name='Mashina bazaga qoshilgan vaqt',auto_now_add=True)
    type = models.ForeignKey(CarTaxiType,on_delete=models.CASCADE,related_name='carTaxi_type')

    def __str__(self):
        return self.name

class CarCargo(models.Model):
    name = models.CharField(verbose_name=_('Yuk mashina turi'),max_length=32)
    height = models.PositiveSmallIntegerField(verbose_name=_('Yuk mashina balandligi'))
    width = models.PositiveSmallIntegerField(verbose_name=_('Yuk mashina eni'))
    length = models.PositiveSmallIntegerField(verbose_name=_('Yuk mashina uzunligi'))
    image = models.ImageField(verbose_name=_('Yuk mashina rasmi'),upload_to='Cargo/image/')
    max_weight = models.PositiveSmallIntegerField(verbose_name=_('Qancha yuk kotara oladi?'))
    number = models.CharField(verbose_name=_('Yuk mashina raqami'), max_length=10)
    price_km = models.PositiveSmallIntegerField(verbose_name='1 km uchun narx')
    created = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(CarDeliveryType, on_delete=models.CASCADE, related_name='carDelivery_type')

    def __str__(self):
        return self.name
