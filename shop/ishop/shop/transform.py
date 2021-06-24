from shop.forms import *
from shop.add_fields_to_category import *


def category_to_form_and_method(category):
    if category == 'Product':
        return add_product_fields_from_form, AddProductForm
    if category == 'Exterior':
        return add_exterior_fields_from_form, AddExteriorForm
    if category == 'Fence':
        return add_fence_fields_from_form, AddFenceForm
    if category == 'GroundCoverage':
        return add_ground_coverage_fields_from_form, AddGroundCoverageForm
    if category == 'Interior':
        return add_interior_fields_from_form, AddInteriorForm
    if category == 'Paint':
        return add_paint_fields_from_form, AddPaintForm
    if category == 'Light':
        return add_light_fields_from_form, AddLightForm
    if category == 'FloorCoverage':
        return add_floor_coverage_fields_from_form, AddFloorCoverageForm
    if category == 'Plumbing':
        return add_plumbing_fields_from_form, AddPlumbingForm
    if category == 'Furniture':
        return add_furniture_fields_from_form, AddFurnitureForm


def category_to_model(category):
    if category == 'Product':
        return Product
    if category == 'Exterior':
        return Exterior
    if category == 'Fence':
        return Fence
    if category == 'GroundCoverage':
        return GroundCoverage
    if category == 'Interior':
        return Interior
    if category == 'Paint':
        return Paint
    if category == 'Light':
        return Light
    if category == 'FloorCoverage':
        return FloorCoverage
    if category == 'Plumbing':
        return Plumbing
    if category == 'Furniture':
        return Furniture
