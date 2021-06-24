from django.db import models

# Create your models here.
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from money.exceptions import MoneyException
from moneyed import *

from accounts.models import Profile


class Wallet(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    created_at = models.DateTimeField(auto_now_add=True)

    def deposit(self, value):
        Transaction.objects.create(
            wallet=self,
            amount=value,
            running_balance=self.balance + value
        )
        self.balance += value
        self.save()

    def withdraw(self, value):
        if value > self.balance:
            raise MoneyException('This wallet has insufficient balance.')

        self.transaction_set.create(
            amount=-value,
            running_balance=self.balance - value
        )
        self.balance -= value
        self.save()

    def transfer(self, wallet, value):
        self.withdraw(value)
        wallet.deposit(value)

    def test(self):
        self.deposit(Money(435, USD))


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    running_balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    created_at = models.DateTimeField(auto_now_add=True)
