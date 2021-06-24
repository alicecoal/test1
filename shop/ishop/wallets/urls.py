from django.conf.urls.static import static

from django.urls import path

from wallets.views import WalletView, dollar

urlpatterns = [
    path('', WalletView.as_view(), name='wallet'),
    path('dollar', dollar, name='zz')
]
