from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from moneyed import USD
from accounts.models import Profile
from shop import models as md
from shop.models.goods import Product


class Cart(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = MoneyField(max_digits=14, decimal_places=2, default_currency=USD)
    created = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total_price = Money(0, USD)

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'

    def remove_itm(self):
        if self.quantity >= 1:
            self.quantity -= 1

    def calc_price(self):
        self.total_price = Money(self.item.price.amount * self.quantity, self.item.price.currency)

    def add_to_cart(self, item, user):
        order_qs = md.Order.objects.filter(user=user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if order.orderitems.filter(item__slug=item.slug).exists():
                self.quantity += 1
                print("This item quantity was updated.")
                self.calc_price()
                self.save()
                return
            else:
                order.orderitems.add(self)
                order.calc_price()
                print(order.total_price)
                order.save()
                print("This item was added to your cart.")
                return
        else:
            order = md.Order.objects.create(
                user=user)
            order.orderitems.add(self)
            order.calc_price()
            print(order.total_price)
            order.save()
            print("This item was added to your cart.")
            return

    def remove_from_avail_cart(self, cart_qs):
        if self.quantity > 1:
            self.quantity -= 1
            self.calc_price()
            self.save()
        else:
            cart_qs.delete()
