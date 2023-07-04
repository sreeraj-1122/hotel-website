from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup,name='signup'),
    path('login', views.loginPage,name='login'),
    path('logout', views.index,name='home'),
    path('home', views.index,name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('rooms', views.rooms,name='rooms'),
    path('service', views.service,name='service'),
    path('booking', views.booking,name='booking'),
    path('viewbooking', views.LogoutPage,name='logout'),
    
   
]
