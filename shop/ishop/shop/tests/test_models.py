import time
import pytest
from django.contrib.auth.models import User

from accounts.models import Profile
from shop.models import Product, Interior, Fence


class TestSuite:

    @pytest.mark.parametrize("test_input,expected", [(Product, "Product"), (Interior, "Interior"), (Fence, "Fence")])
    def test_eval(self, test_input, expected):
        test_input.objects.create(name="Test")
        assert test_input.category == expected
