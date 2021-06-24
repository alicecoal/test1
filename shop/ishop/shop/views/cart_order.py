import stripe
import logging
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from shop.models import *

stripe.api_key = settings.STRIPE_SECRET_KEY
logger = logging.getLogger(__name__)


@login_required()
def buy(request):
    current_order = Order.objects.filter(user=request.user.profile)[0]
    if current_order.buy() == 'deny':
        logger.warning("Fail buy for {}".format(request.user.profile.get_profile()))
        return HttpResponseRedirect('../shop/deny')
    logger.info("Successful buy for {}".format(request.user.profile.get_profile()))
    return HttpResponseRedirect('../shop/approve')


@login_required()
def delete_order(request):
    current_order = Order.objects.filter(user=request.user.profile)
    current_order.delete()
    logger.info("Order deleted: {}".format(current_order))
    return redirect("..")


@login_required()
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    user = request.user.profile.get_profile()
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user.profile.get_profile()
    )
    order_item.add_to_cart(item, user)
    logger.info("Order of {} successful added for: {}".format(item, user))
    return redirect("..")


def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user.profile, item=item)
    if cart_qs.exists():
        current_cart = cart_qs[0]
        current_cart.remove_from_avail_cart(cart_qs)
    order_qs = Order.objects.filter(
        user=request.user.profile,
        ordered=False
    )
    if order_qs.exists():
        current_order = order_qs[0]
        current_order.remove_current_order(item, request.user.profile)
        logger.info("Order of {} successful deleted for: {}".format(item, request.user.profile))
        return redirect("..")
    else:
        logger.info("Order of {} successful deleted for: {}".format(item, request.user.profile))
        return redirect("..")
