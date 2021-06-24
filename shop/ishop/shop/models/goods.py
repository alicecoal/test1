from django.db import models
from djmoney.models.fields import MoneyField
from shop import settings

CATEGORY_CHOICES = (
    ('Product', 'Product'),
    ('Interior', 'Interior'),
    ('Exterior', 'Exterior'),
    ('GroundCoverage', 'GroundCoverage'),
    ('Fence', 'Fence'),
    ('Paint', 'Paint'),
    ('Light', 'Light'),
    ('FloorCoverage', 'FloorCoverage'),
    ('Plumbing', 'Plumbing'),
    ('Furniture', 'Furniture'),
)


class Product(models.Model):
    slug = models.AutoField(primary_key=True)
    category = models.CharField(max_length=15, verbose_name='Category', choices=CATEGORY_CHOICES, default="Product")
    img = models.ImageField(upload_to='shop', blank=False)
    name = models.CharField(max_length=300)
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    discount_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category = self.class_name()

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return self.name

    def get_template_img(self):
        print(self.img.path.replace('shop/', ''))

    def get_value(self):
        return [self.slug, self.category, self.name, self.preview_text, self.detail_text, self.price,
                self.discount_price, self.seller]

    @staticmethod
    def count_value():
        return 8


class Exterior(Product):
    is_water_prooved = models.BooleanField(default=False)
    brand = models.TextField(max_length=200, verbose_name='Brand name')


class GroundCoverage(Exterior):
    sport_compatibility = models.BooleanField(default=False)
    warranty = models.IntegerField(default=0)


class Fence(Exterior):
    is_three_dim = models.BooleanField(default=False)
    type = models.TextField(max_length=200, verbose_name='Type')


class Interior(Product):
    warranty = models.IntegerField(default=0)
    child_compatibility = models.BooleanField(default=False)


class Plumbing(Interior):
    capacity = models.IntegerField(default=0)
    # better to enum !
    type = models.TextField(max_length=200, verbose_name='Type')


class Light(Interior):
    power = models.IntegerField(default=0)
    # better to enum !
    style = models.TextField(max_length=200, verbose_name='Type')
    lux = models.IntegerField(default=0)
    temperature = models.IntegerField(default=0)


class FloorCoverage(Interior):
    vacuum_compatibility = models.BooleanField(default=False)
    # better to enum !
    type = models.TextField(max_length=200, verbose_name='Type')
    brand = models.TextField(max_length=200, verbose_name='Brand')
    fits_for = models.TextField(max_length=200, verbose_name='Main coverage material')


class Paint(Interior):
    painter = models.TextField(max_length=200, verbose_name='Name of painter')
    style = models.TextField(max_length=200, verbose_name='Style')
    year = models.IntegerField(default=0)


class Furniture(Interior):
    pet_compatibility = models.BooleanField(default=False)
    # better to enum !
    type = models.TextField(max_length=200, verbose_name='Type')
    brand = models.TextField(max_length=200, verbose_name='Brand')
    style = models.TextField(max_length=200, verbose_name='Style')