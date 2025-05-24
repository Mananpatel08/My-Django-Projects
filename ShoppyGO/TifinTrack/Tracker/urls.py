from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wallet-history/' , views.wallet_history, name="wallets" ),
    path('track-history/' , views.track_history , name="track" )
]