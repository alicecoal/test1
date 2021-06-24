from django.template.context_processors import request
from django.views.generic import RedirectView, TemplateView
from django.urls import path

from .views import *


urlpatterns = [
    path('', HomeView.as_view(model=Product), name='home'),
    path('fence', HomeView.as_view(model=Fence), name='fence'),
    path('furniture', HomeView.as_view(model=Furniture), name='furniture'),
    path('paint', HomeView.as_view(model=Paint), name='paint'),
    path('interior', HomeView.as_view(model=Interior), name='interior'),
    path('exterior', HomeView.as_view(model=Exterior), name='exterior'),
    path('ground_coverage', HomeView.as_view(model=GroundCoverage), name='ground_coverage'),
    path('floor_coverage', HomeView.as_view(model=FloorCoverage), name='floor_coverage'),
    path('light', HomeView.as_view(model=Light), name='light'),
    path('plumbing', HomeView.as_view(model=Plumbing), name='plumbing'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('cart', BuyView.as_view(model=Cart, template_name="shop/cart.html"), name='cart_all'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
    path('order', BuyView.as_view(model=Order, template_name="shop/order.html"), name='order'),
    path('None', RedirectView.as_view(pattern_name='shop:home'), name='buy'),
    path('shop', RedirectView.as_view(pattern_name='shop:home'), name='redirect'),
    path('add',  add_category, name='add'),
    path('add_product/<category>',  add_product, name='add_product'),
    path('delete/<slug>', delete_item, name='delete_item'),
    path('edit/<slug>/<category>', edit_product, name='edit_product'),
    path('deny', TemplateView.as_view(template_name='shop/deny.html'), name='deny'),
    path('approve', TemplateView.as_view(template_name='shop/approve.html'), name='approve'),
    path('export', create_report, name='export'),
    path('admin', create_admin_report, name='admin'),
    path('buy', buy, name='buy'),
    path('<slug>', ShowView.as_view(model=Product), name='show'),
    path('delete_order', delete_order, name='delete_order')
]
