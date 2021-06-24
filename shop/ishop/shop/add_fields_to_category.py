def add_product_fields_from_form(product, form, user, category):
    product.category = form.cleaned_data.get('category')
    product.name = form.cleaned_data.get('name')
    product.img = form.cleaned_data.get('img')
    product.detail_text = form.cleaned_data.get('detail_text')
    product.preview_text = form.cleaned_data.get('preview_text')
    product.price = form.cleaned_data.get('price')
    product.discount_price = form.cleaned_data.get('discount_price')
    product.seller = user
    product.category = category


def add_exterior_fields_from_form(exterior, form, user, category):
    add_product_fields_from_form(exterior, form, user, category)
    exterior.is_water_prooved = form.cleaned_data.get('is_water_prooved')
    exterior.brand = form.cleaned_data.get('brand')


def add_fence_fields_from_form(fence, form, user, category):
    add_exterior_fields_from_form(fence, form, user, category)
    fence.is_three_dim = form.cleaned_data.get('is_three_dim')
    fence.type = form.cleaned_data.get('type')


def add_ground_coverage_fields_from_form(ground_coverage, form, user, category):
    add_exterior_fields_from_form(ground_coverage, form, user, category)
    ground_coverage.sport_compatibility = form.cleaned_data.get('sport_compatibility')
    ground_coverage.warranty = form.cleaned_data.get('warranty')


def add_interior_fields_from_form(interior, form, user, category):
    add_product_fields_from_form(interior, form, user, category)
    interior.child_compatibility = form.cleaned_data.get('child_compatibility')
    interior.warranty = form.cleaned_data.get('warranty')


def add_plumbing_fields_from_form(plumbing, form, user, category):
    add_interior_fields_from_form(plumbing, form, user, category)
    plumbing.capacity = form.cleaned_data.get('capacity')
    plumbing.type = form.cleaned_data.get('type')


def add_light_fields_from_form(light, form, user, category):
    add_interior_fields_from_form(light, form, user, category)
    light.power = form.cleaned_data.get('power')
    light.lux = form.cleaned_data.get('lux')
    light.temperature = form.cleaned_data.get('temperature')


def add_floor_coverage_fields_from_form(floor_coverage, form, user, category):
    add_interior_fields_from_form(floor_coverage, form, user, category)
    floor_coverage.vacuum_compatibility = form.cleaned_data.get('vacuum_compatibility')
    floor_coverage.type = form.cleaned_data.get('type')
    floor_coverage.brand = form.cleaned_data.get('brand')
    floor_coverage.fits_for = form.cleaned_data.get('fits_for')


def add_paint_fields_from_form(paint, form, user, category):
    add_interior_fields_from_form(paint, form, user, category)
    paint.painter = form.cleaned_data.get('painter')
    paint.style = form.cleaned_data.get('style')
    paint.year = form.cleaned_data.get('year')


def add_furniture_fields_from_form(furniture, form, user, category):
    add_interior_fields_from_form(furniture, form, user, category)
    furniture.pet_compatibility = form.cleaned_data.get('pet_compatibility')
    furniture.type = form.cleaned_data.get('type')
    furniture.brand = form.cleaned_data.get('brand')
    furniture.style = form.cleaned_data.get('style')
