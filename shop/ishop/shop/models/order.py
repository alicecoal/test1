from datetime import date

from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from money.exceptions import MoneyException
from moneyed import USD

from accounts.models import Profile
from shop import models as md
from shop.models.helpers import Event, singleton, Observer, decorator
from wallets.models import Wallet


class Order(models.Model):
    orderitems = models.ManyToManyField(md.Cart)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    total_price = MoneyField(max_digits=14, decimal_places=2, default_currency=USD)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total_price = Money(0, USD)

    def __str__(self):
        return str(self.user.user) + " " + str(self.created)

    def show_order(self):
        return ', '.join([temp.item.name for temp in self.orderitems.all()])

    def calc_price(self):
        self.total_price = self.show_price()

    def show_price(self):
        print(self.orderitems.all())
        price = Money(0, USD)
        for elem in self.orderitems.all():
            elem.calc_price()
            elem.save()
            print(elem.total_price)
            price += elem.total_price
        return price

    def buy(self):
        print(self)
        inspector = Inspector()
        inspector.observe('inspector_step', inspector.inspector_step)
        inspector.observe('value_step', inspector.value_step)

        print(inspector.__dict__)
        print(id(inspector))
        order = self
        Event('inspector_step', 1)
        Event('value_step', order)
        print(id(inspector))
        print(inspector.__dict__)
        print('------------------')
        wallets = Wallet.objects.filter(user=self.user.user.profile)
        wallet = wallets[0]
        for temp_wallet in wallets:
            if temp_wallet.balance.currency == self.show_price().currency:
                wallet = temp_wallet
        try:
            print("---RECEIPT---")
            print(wallet.balance)
            wallet.withdraw(self.show_price())
            print(wallet.balance)
            print("---RECEIPT---")
        except MoneyException:
            print("No balance")
            return 'deny'
        except TypeError:
            print("Can't do this")
            return 'deny'
        else:
            print("Successful")
            return 'approve'

    def remove_current_order(self, item, user):
        if self.orderitems.filter(item__slug=item.slug).exists():
            order_item = md.Cart.objects.filter(
                item=item,
                user=user,
            )[0]
            self.orderitems.remove(order_item)
            self.calc_price()
            print("This item was removed from your cart.")
            return
        else:
            print("This item was not in your cart")
            return


@singleton
class Inspector(Observer):
    counter: int
    value: Money
    day: date

    def __init__(self):
        Observer.__init__(self)
        self.counter = 0
        self.value = Money(0, USD)
        self.day = date.today()
        print('INIT')

    @decorator
    def inspector_step(self, counter):
        self.counter += counter
        return self.counter

    def value_step(self, order: Order):
        order.calc_price()
        self.value += order.total_price
        # print('Got value')
        # print(self.value)
        return
