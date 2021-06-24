from django.contrib import admin

# Register your models here.
from shop.models import *

admin.site.register(Product)

admin.site.register(Interior)
admin.site.register(Exterior)

admin.site.register(Plumbing)
admin.site.register(Furniture)
admin.site.register(Paint)
admin.site.register(Fence)
admin.site.register(GroundCoverage)
admin.site.register(FloorCoverage)
admin.site.register(Light)

admin.site.register(Cart)
admin.site.register(Order)
