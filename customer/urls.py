from django.urls import path
from .views import *




urlpatterns = [
    path('', Index.as_view(), name='index' ),
    path('about/', About.as_view(), name='about' ),
    path('order/', Order.as_view(), name='order' ),
    path('order-confirmation/<int:pk>', OrderConfirmation.as_view(), name='order-confirmation' ),
    path('payment-confirmation/', OrderPayConfirmation.as_view(), name='payment-confirmation' ),
    path('menu/', Menu.as_view(), name='menu'),
    path('menu/search/', MenuSearch.as_view(), name='menu-search'),
    path('logout', user_logout, name='logout'),
    
]
