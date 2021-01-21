from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "^mm-24*i-6iecm7c@z9l+7%^ns^4g^z!8=dgffg4ulggr-4=1%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

APIS_BASE_URI = "https://richardapis/"
INSTALLED_APPS += ["gm2m", "apis_highlighter", "django_extensions", "apis_ipif2"]
APIS_RELATIONS_FILTER_EXCLUDE += ["annotation", "annotation_set_relation"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "db",
        "USER": "user",
        "PASSWORD": "password",
        "HOST": "127.0.0.1",  # Or an IP Address that your DB is hosted on
        "PORT": "3306",
    }
}
