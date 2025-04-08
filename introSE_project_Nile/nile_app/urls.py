from django.urls import path
from . import views

urlpatterns = [
    path('', views.nileHomePage, name='nileHomePage'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    path('nileAccountInfo', views.nileAccountInfo, name='nileAccountInfo'),
    path('nileCreateAccount', views.nileCreateAccount, name='nileCreateAccount'),
    path('nileProducts', views.nileProducts, name='nileProducts'),
    path('nileLogin', views.nileLogin, name='nileLogin'),
    path('nileAccountDeletion', views.nileAccountDeletion, name='nileAccountDeletion'),
    path('nileAccountSettings', views.nileAccountSettings, name='nileAccountSettings')
]