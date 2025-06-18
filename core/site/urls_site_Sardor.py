from django.urls import path
from .views_site_Sardor import taxi,delivery
from .views_site_Alijon import index,cargo

urlpatterns = [
    path('',index,name='home'),
    path('cargo/',cargo,name='cargo'),
    path('taxi/',taxi,name='taxi'),
    path('delivery/',delivery,name='delivery'),
]