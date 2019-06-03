"""
Django settings for mpr project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(os.path.join(__file__, "../")))
)

SHARED_URL = "https://shared.acdh.oeaw.ac.at/"

ACDH_IMPRINT_URL = "https://shared.acdh.oeaw.ac.at/acdh-common-assets/api/imprint.php?serviceID="

PROJECT_NAME = "apis"
PROJECT_SHARED = "https://shared.acdh.oeaw.ac.at/apis/"
PROJECT_DEFAULT_MD = {
    'title': 'TITLE',
    'author': 'Matthias Schlögl, Peter Andorfer',
    'subtitle': 'SUBTITLE',
    'description': """This is a default metadata file. To change this, provide\
    provide a following file {PROJECT_SHARED}/{PROJECT_NAME}/metadata.json""",
    'github': 'https://github.com/acdh-oeaw/apis-webpage-base',
    'production instance': None,
    'purpose_de': '',
    'purpose_en': """""",
    'version': ['apis_core', 'charts', 'django'],
    'matomo_id': '',
    'matomo_url': '',
    'imprint': '/imprint',
    'social_media': [
        ('fab fa-twitter', 'https://twitter.com/ACDH_OeAW'),
        ('fab fa-youtube', 'https://www.youtube.com/channel/UCgaEMaMbPkULYRI5u6gvG-w'),
    ],
    'social_media': [
        ('fab fa-twitter fa-2x', 'https://twitter.com/ACDH_OeAW'),
        ('fab fa-youtube fa-2x', 'https://www.youtube.com/channel/UCgaEMaMbPkULYRI5u6gvG-w'),
    ],
    'app_type': 'database',
}

# Application definition

INSTALLED_APPS = [
    "dal",
    # 'corsheaders',
    "dal_select2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "reversion",
    "reversion_compare",
    "crispy_forms",
    "django_filters",
    "django_tables2",
    "rest_framework",
    "webpage",
    "browsing",
    "django_extensions",
    "apis_core.apis_entities",
    "apis_core.apis_metainfo",
    "apis_core.apis_relations",
    "apis_core.apis_vocabularies",
    "apis_core.apis_labels",
    # 'apis_core.apis_vis',
    "rest_framework.authtoken",
    "guardian",
    "charts",
    "infos",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ("GET", "OPTIONS")


CRISPY_TEMPLATE_PACK = "bootstrap3"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 50,
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
}

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",  # this is default
    "guardian.backends.ObjectPermissionBackend",
)

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "reversion.middleware.RevisionMiddleware",
]

ROOT_URLCONF = "apis.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "webpage.webpage_content_processors.installed_apps",
                "webpage.webpage_content_processors.is_dev_version",
                "webpage.webpage_content_processors.get_db_name",
                "webpage.webpage_content_processors.title_img",
                "webpage.webpage_content_processors.logo_img",
                "webpage.webpage_content_processors.custom_css",
                "webpage.webpage_content_processors.shared_url",
                "webpage.webpage_content_processors.apis_app_name",
                "apis_core.context_processors.custom_context_processors.add_entities",
                "apis_core.context_processors.custom_context_processors.add_relations",
                "apis_core.context_processors.custom_context_processors.add_apis_settings",
            ]
        },
    }
]

WSGI_APPLICATION = "apis.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

APIS_BASE_URI = "TO CHANGE"

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"

DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"

APIS_COMPONENTS = []
# APIS settings

APIS_TEI_TEXTS = ["xml/tei transcription"]
APIS_CETEICEAN_CSS = "https://teic.github.io/CETEIcean/css/CETEIcean.css"
APIS_CETEICEAN_JS = "https://teic.github.io/CETEIcean/js/CETEI.js"

APIS_NEXT_PREV = True

APIS_ALTERNATE_NAMES = [
    "Taufname",
    "Ehename",
    "Name laut ÖBL XML",
    "alternative Namensform",
    "alternative name",
    "Künstlername",
    "Mädchenname",
    "Pseudonym",
    "weitere Namensform",
]

APIS_RELATIONS_FILTER_EXCLUDE = [
    "uri",
    "tempentityclass",
    "user",
    "__id",
    "source",
    "label",
    "temp_entity",
    "collection__",
    "_ptr",
    "baseclass",
    "id",
    "written",
    "relation_type__description",
    "relation_type__parent_class",
    "relation_type__status",
    "relation_type__vocab_name",
    "relation_type__name_reverse",
    "__text",
]

APIS_RELATIONS = {
    "list_filters": [("relation_type",)],
    "search": ["relation_type__name"],
    "exclude": ["name"],
    "PersonPlace": {
        "labels": ["related_person", "related_place", "relation_type"],
        "search": [
            "relation_type__name",
            "related_person__name",
            "related_person__first_name",
            "related_place__name",
        ],
        "list_filters": [("relation_type",), ("related_person",), ("related_place",)],
    },
    "PersonInstitution": {
        "labels": ["related_person", "related_institution", "relation_type"],
        "search": [
            "relation_type__name",
            "related_person__name",
            "related_person__first_name",
            "related_institution__name",
        ],
        "list_filters": [
            ("relation_type",),
            ("related_person",),
            ("related_institution",),
        ],
    },
    "PersonEvent": {
        "labels": ["related_person", "related_event", "relation_type"],
        "search": [
            "relation_type__name",
            "related_person__name",
            "related_person__first_name",
            "related_event__name",
        ],
        "list_filters": [("relation_type",), ("related_person",), ("related_event",)],
    },
    "PersonWork": {
        "labels": ["related_person", "related_work", "relation_type"],
        "search": [
            "relation_type__name",
            "related_person__name",
            "related_person__first_name",
            "related_work__name",
        ],
        "list_filters": [("relation_type",), ("related_person",), ("related_work",)],
    },
    "PersonPerson": {
        "labels": ["related_personA", "related_personB", "relation_type"],
        "search": [
            "relation_type__name",
            "related_personA__name",
            "related_personA__first_name",
            "related_personB__name",
            "related_personB__first_name",
        ],
        "list_filters": [
            ("relation_type",),
            ("related_personA",),
            ("related_personB",),
        ],
    },
    "InstitutionPlace": {
        "labels": ["related_institution", "related_place", "relation_type"],
        "search": [
            "relation_type__name",
            "related_institution__name",
            "related_place__name",
        ],
        "list_filters": [
            ("relation_type",),
            ("related_institution",),
            ("related_place",),
        ],
    },
    "InstitutionWork": {
        "labels": ["related_institution", "related_work", "relation_type"],
        "search": [
            "relation_type__name",
            "related_institution__name",
            "related_work__name",
        ],
        "list_filters": [
            ("relation_type",),
            ("related_institution",),
            ("related_work",),
        ],
    },
    "InstitutionEvent": {
        "labels": ["related_institution", "related_event", "relation_type"],
        "search": [
            "relation_type__name",
            "related_institution__name",
            "related_event__name",
        ],
        "list_filters": [
            ("relation_type",),
            ("related_institution",),
            ("related_event",),
        ],
    },
    "InstitutionInstitution": {
        "labels": ["related_institutionA", "related_institutionB", "relation_type"],
        "search": [
            "relation_type__name",
            "related_institutionA__name",
            "related_institutionB__name",
        ],
        "list_filters": [
            ("relation_type",),
            ("related_institutionA",),
            ("related_institutionB",),
        ],
    },
    "PlaceWork": {
        "labels": ["related_work", "related_place", "relation_type"],
        "search": ["relation_type__name", "related_place__name", "related_work__name"],
        "list_filters": [("relation_type",), ("related_place",), ("related_work",)],
    },
    "PlaceEvent": {
        "labels": ["related_event", "related_place", "relation_type"],
        "search": ["relation_type__name", "related_place__name", "related_event__name"],
        "list_filters": [("relation_type",), ("related_place",), ("related_event",)],
    },
    "PlacePlace": {
        "labels": ["related_placeA", "related_placeB", "relation_type"],
        "search": [
            "relation_type__name",
            "related_placeA__name",
            "related_placeB__name",
        ],
        "list_filters": [("relation_type",), ("related_placeA",), ("related_placeB",)],
    },
    "EventWork": {
        "labels": ["related_event", "related_work", "relation_type"],
        "search": ["relation_type__name", "related_event__name", "related_work__name"],
        "list_filters": [("relation_type",), ("related_event",), ("related_work",)],
    },
    "EventEvent": {
        "labels": ["related_eventA", "related_eventB", "relation_type"],
        "search": [
            "relation_type__name",
            "related_eventA__name",
            "related_eventB__name",
        ],
        "list_filters": [("relation_type",), ("related_eventA",), ("related_eventB",)],
    },
    "WorkWork": {
        "labels": ["related_workA", "related_workB", "relation_type"],
        "search": ["relation_type__name", "related_workA__name", "related_workB__name"],
        "list_filters": [("relation_type",), ("related_workA",), ("related_workB",)],
    },
}

APIS_VOCABULARIES = {"exclude": ["userAdded"]}

APIS_ENTITIES = {
    "Place": {
        "search": ["name"],
        "table_fields": ["name"],
        "additional_cols": ["lat", "lng", "part_of"],
        "list_filters": [
            ("name", {"method": "wildcard_filter", "label": "Name"}),
            ("status", {"method": "wildcard_filter", "label": "Status"}),
            ("collection", {"label": "Collection"}),
        ],
    },
    "Person": {
        "merge": True,
        "search": ["name", "first_name"],
        "form_order": ["first_name", "name"],
        "table_fields": ["name", "first_name", "start_date", "end_date"],
        "additional_cols": ["profession", "gender"],
        "list_filters": [
            ("name", {"method": "name_label_filter", "label": "Name complete"}),
            ("first_name", {"method": "wildcard_filter", "label": "Firstname"}),
            ("gender", {"label": "Gender"}),
            ("start_date", {"label": "Date of Birth"}),
            ("end_date", {"label": "Date of Death"}),
            ("profession", {"label": "Profession"}),
            ("collection", {"label": "Collection"}),
        ],
        "api_exclude": [],
    },
    "Institution": {
        "search": ["name"],
        "list_filters": [
            ("name", {"method": "wildcard_filter", "label": "Name"}),
            ("start_date", {"label": "Date of foundation"}),
            ("end_date", {"label": "Date of termination"}),
            ("collection", {"label": "Collection"}),
        ],
    },
    "Work": {
        "search": ["name"],
        "list_filters": [("name", {"method": "wildcard_filter", "label": "Name"})],
    },
    "Event": {
        "search": ["name"],
        "list_filters": [("name", {"method": "wildcard_filter", "label": "Name"})],
    },
}


APIS_LIST_VIEWS_ALLOWED = False
APIS_DETAIL_VIEWS_ALLOWED = False

APIS_LIST_VIEW_TEMPLATE = "browsing/generic_list.html"
APIS_DELETE_VIEW_TEMPLATE = "webpage/confirm_delete.html"

APIS_IIIF_WORK_KIND = "IIIF"
APIS_IIIF_ENT_IIIF_REL = "has iiif image"
APIS_IIIF_SERVER = "https://iiif.acdh.oeaw.ac.at/"
APIS_OSD_JS = (
    "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/2.4.0/openseadragon.min.js"
)
APIS_OSD_IMG_PREFIX = (
    "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/2.4.0/images/"
)
