from django.db import models
from django.utils.translation import gettext_lazy as _
# from .models_auth import User

class Brand(models.Model):
    name = models.CharField(verbose_name='Mashina brandi',max_length=32)
    img = models.ImageField(verbose_name='Mashina brandi rasmi',upload_to='/brand_img')


    def __str__(self):
        return self.name

class Driver(models.Model):
    fio = models.CharField(verbose_name='Haydovchini fiosi')
    phone = models.CharField(verbose_name='Haydovchini telefoni')

    def __str__(self):
        return self.fio


class CarDelivery(models.Model):
    name = models.CharField(verbose_name=_('Mashina turi'),max_length=32)
    height = models.PositiveSmallIntegerField(verbose_name=_('Mashina balandligi'))
    width = models.PositiveSmallIntegerField(verbose_name=_('Mashina eni'))
    length = models.PositiveSmallIntegerField(verbose_name=_('Mashina uzunligi'))
    image = models.ImageField(verbose_name=_('Mashina rasmi'),upload_to='Car/image/')
    max_weight = models.PositiveSmallIntegerField(verbose_name=_('Qancha yuk kotara oladi?'))
    number = models.CharField(verbose_name=_('Mashina raqami'), max_length=10)
    price_km = models.PositiveSmallIntegerField(verbose_name='1 km uchun narx')
    created = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='carDelivery_brand')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='carDelivery_brand')



class CarTaxiType(models.Model):
    name = models.CharField(default=1,choices=[
        (1,'Ekanom'),
        (2,'Komfort'),
        (3,'Lux'),
    ])

    def __str__(self):
        return self.name


class CarTaxi(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='carTaxi_brand')
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,related_name='carTaxi_brand')
    type = models.ForeignKey(CarTaxiType,on_delete=models.CASCADE,related_name='carTaxi_type')
