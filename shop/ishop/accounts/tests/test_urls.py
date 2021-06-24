import pytest
from django.urls import reverse
from requests import get


class TestSuite:
    @pytest.mark.urls("accounts.urls")
    def test_login_page(self):
        uri = reverse('login')
        assert 'login' in uri

    @pytest.mark.urls("accounts.urls")
    def test_profile_page(self):
        uri = reverse('profile')
        assert '' in uri
