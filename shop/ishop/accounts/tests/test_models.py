import time
import pytest
from django.contrib.auth.models import User

from accounts.models import Profile


class TestSuite:

    @pytest.mark.django_db(transaction=True)
    def test_should_check_password(self):
        me = Profile.user.objects.get(username='ann')
        assert me.is_superuser

    @pytest.mark.django_db
    def test_should_create_profile(self):
        user = User.objects.create(username='test_test')
        profile = Profile.objects.create(user=user)
        profile.age = 18
        assert Profile.objects.all().filter(age=18, user=user)[0] == profile

    def test_should_edit_profile(self):
        user = User.objects.create(username='test_test')
        profile = Profile.objects.create(user=user)
        profile.age = 18
        profile_to_change = Profile.objects.all().filter(age=18, user=user)[0]
        profile_to_change.age = 25
        profile_to_change.save()
        assert Profile.objects.all().filter(age=25, user=user)[0] == profile_to_change

    def test_should_delete_profile(self):
        user = User.objects.create(username='test_test')
        profile = Profile.objects.create(user=user)
        profile.age = 18
        profile_to_change = Profile.objects.all().filter(age=18, user=user)[0]
        profile_to_change.delete()
        assert not Profile.objects.all().filter(age=18, user=user).exists()
