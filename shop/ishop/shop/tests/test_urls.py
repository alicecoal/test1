import pytest
from django.urls import reverse


class TestSuite:
    @pytest.mark.urls("shop.urls")
    def test_login_page(self):
        uri = reverse('cart', kwargs={'slug': 4})
        assert 'cart/4' in uri

    @pytest.mark.urls("shop.urls")
    @pytest.mark.parametrize("slug, category, expected",
                             [(4, 'Product', "edit/4/Product"),
                              (5, 'Exterior', "edit/5/Exterior"),
                              (7, 'Fence', "edit/7/Fence")])
    def test_profile_page(self, slug, category, expected):
        uri = reverse('edit_product', kwargs={'slug': slug, 'category': category})
        assert expected in uri
