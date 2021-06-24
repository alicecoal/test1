from django import forms
from django.forms import BaseModelForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from djmoney.models.fields import MoneyField
from djmoney.money import Money

from shop.models import *


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('img', 'name', 'preview_text', 'detail_text', 'price', 'discount_price',)


class AddExteriorForm(forms.ModelForm):
    class Meta:
        model = Exterior
        fields = ('img', 'name', 'preview_text', 'detail_text', 'price', 'discount_price',
                  'is_water_prooved', 'brand',)


class AddGroundCoverageForm(forms.ModelForm):
    class Meta:
        model = GroundCoverage
        fields = ('img', 'name', 'preview_text', 'detail_text', 'price',
                  'discount_price', 'is_water_prooved', 'brand',
                  'sport_compatibility', 'warranty',)


class AddFenceForm(forms.ModelForm):
    class Meta:
        model = Fence
        fields = ('img', 'name', 'preview_text', 'detail_text', 'price',
                  'discount_price', 'is_water_prooved', 'brand',
                  'is_three_dim', 'type',)


class AddInteriorForm(forms.ModelForm):
    class Meta:
        model = Interior
        fields = ('img', 'name', 'preview_text', 'detail_text', 'price',
                  'discount_price', 'warranty', 'child_compatibility',)


class AddPlumbingForm(forms.ModelForm):
    class Meta:
        model = Plumbing
        fields = ('img', 'name', 'preview_text', 'detail_text', 'price',
                  'discount_price', 'warranty', 'child_compatibility',
                  'capacity', 'type',)


class AddLightForm(forms.ModelForm):
    class Meta:
        model = Light
        fields = ('img', 'name', 'preview_text', 'detail_text', 'price',
                  'discount_price', 'warranty', 'child_compatibility',
                  'power', 'style', 'temperature', 'lux',)


class AddFloorCoverageForm(forms.ModelForm):
    class Meta:
        model = FloorCoverage
        fields = ('img', 'name', 'preview_text', 'detail_text', 'price',
                  'discount_price', 'warranty', 'child_compatibility',
                  'vacuum_compatibility', 'type', 'brand', 'fits_for',)


class AddPaintForm(forms.ModelForm):
    class Meta:
        model = Paint
        fields = ('img', 'name', 'preview_text', 'detail_text', 'price',
                  'discount_price', 'warranty', 'child_compatibility',
                  'painter', 'style', 'year',)


class AddFurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ('img', 'name', 'preview_text', 'detail_text', 'price',
                  'discount_price', 'warranty', 'child_compatibility',
                  'pet_compatibility', 'type', 'brand', 'style',)


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category',)