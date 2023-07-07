from django.urls import path
from . import views
urlpatterns = [
    #path('',views.index,name='index'),
    path('',views.home, name='home'),
    path('base',views.base, name='base'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('portfolio',views.portfolio, name='portfolio'),
    path('services',views.services, name='services'),
    
    
    
]
 