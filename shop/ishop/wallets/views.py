from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from wallets.models import Wallet


class WalletView(ListView):
    model = Wallet
    template_name = 'wallet/wallet.html'


def dollar(request):
    wallets = Wallet.objects.filter(user=request.user.profile)
    for wallet in wallets:
        print(wallet.balance)
    wallets[0].test()
    return HttpResponse('Successful')
