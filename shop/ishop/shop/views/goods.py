import logging

import stripe
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from shop.forms import *
from shop.models import *
from shop.transform import category_to_form_and_method, category_to_model
from shop.add_fields_to_category import *

stripe.api_key = settings.STRIPE_SECRET_KEY
logger = logging.getLogger(__name__)


class HomeView(ListView):
    model = Product
    paginate_by = 10
    ordering = 'slug'
    template_name = "shop/index.html"

class ShowView(DetailView):
    model = Product

class BuyView(ListView):
    model = Product
    template_name = "shop/index.html"


@login_required()
def add_category(request):
    if not request.user.profile.get_profile().is_seller:
        return HttpResponseRedirect('../shop')
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('../shop/add_product/{}'.format(form.data.get('category')))
    else:
        form = AddCategoryForm()
    return render(request, 'shop/add_category.html', {'form': form})


@login_required()
def add_product(request, category):
    if not request.user.profile.get_profile().is_seller:
        logger.warning("{} tried to get access to add product".format(request.user.profile.get_profile()))
        return HttpResponseRedirect('../shop')
    add_specified_fields, form_of_category = category_to_form_and_method(category)
    if request.method == 'POST':
        form = form_of_category(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            add_specified_fields(product, form, request.user.profile, category)
            logger.info("Successful added product {} by {}".format(product, request.user.profile.get_profile()))
            return HttpResponseRedirect('../../shop')
    else:
        form = form_of_category()
    return render(request, 'shop/add_product.html', {'form': form})


@login_required()
def delete_item(request, slug):
    item = get_object_or_404(Product, slug=slug)
    if not item.seller == request.user.profile.get_profile():
        logger.info("Failed delete product {} by {}".format(item, request.user.profile.get_profile()))
        return HttpResponseRedirect('..')
    item.delete()
    logger.info("Successful deleted product {} by {}".format(item, request.user.profile.get_profile()))
    return HttpResponseRedirect('..')


@login_required()
def edit_product(request, slug, category):
    item = get_object_or_404(category_to_model(category), slug=slug)
    if not item.seller == request.user.profile.get_profile():
        return HttpResponseRedirect('..')
    add_specified_fields, form_of_category = category_to_form_and_method(category)
    if request.method == 'POST':
        form = form_of_category(request.POST, request.FILES, instance=item)
        if form.is_valid():
            product = item
            add_specified_fields(product, form, request.user.profile, category)
            product.save()
            logger.info("Successful edited product {} with id {} by {}".format(product, product.slug,
                                                                               request.user.profile.get_profile()))
            return HttpResponseRedirect('../../shop')
    else:
        form = form_of_category(instance=item)
    return render(request, 'shop/add_product.html', {'form': form})
