from django.urls import path,include


urlpatterns = [
    path('auth/',include('core.auth.urls_auth')),
    path('',include('core.site.urls_site_Sardor')),

]