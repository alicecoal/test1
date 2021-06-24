from distutils.command.config import config

MEDIA_URL = 'media/'
MEDIA_ROOT = 'media/'

AUTH_PROFILE_MODULE = 'accounts.Profile'
AUTH_USER_MODEL = 'accounts.Profile'


def STRIPE_SECRET_KEY():
    return None
