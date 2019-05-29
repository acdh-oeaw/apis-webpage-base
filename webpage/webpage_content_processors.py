from django.conf import settings
from . utils import PROJECT_METADATA
from . utils import PROJECT_TITLE_IMG, PROJECT_LOGO


def title_img(request):
    return {'PROJECT_TITLE_IMG': PROJECT_TITLE_IMG}


def logo_img(request):
    return {'PROJECT_LOGO': PROJECT_LOGO}


def installed_apps(request):
    return {'APPS': settings.INSTALLED_APPS}


def is_dev_version(request):
    try:
        return {'DEV_VERSION': settings.DEV_VERSION}
    except AttributeError:
        return {}


def get_db_name(request):
    try:
        db_name = settings.DATABASES['default']['NAME']
        return {'DB_NAME': db_name}
    except Exception as e:
        return {}
