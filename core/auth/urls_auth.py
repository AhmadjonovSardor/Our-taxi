from django.urls import path

from .views_auth import register,log_in,log_out

urlpatterns = [
    path('regis/', register,name='regis'),
    path('in/', log_in,name='in'),
    path('out', log_out, name="out"),
]