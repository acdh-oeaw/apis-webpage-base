"""
Django settings for mpr project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from typing import Dict, Any

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
    "apis_core.apis_entities",
    "apis_core.apis_metainfo",
    "apis_core.apis_relations",
    "apis_core.apis_vocabularies",
    "apis_core.apis_labels",
    # 'apis_core.apis_vis',
    "rest_framework.authtoken",
    #"drf_yasg",
    "drf_spectacular",
    "guardian",
    "charts",
    "infos",
    "django_summernote",
]

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ("GET", "OPTIONS")

SPECTACULAR_SETTINGS: Dict[str, Any] = {
'TITLE': 'APIS generic API',
'DESCRIPTIOPN': 'Provides access to the main APIS data-model endpoints.',
'LICENSE': {'name': 'MIT License', 'url': 'https://www.mit.edu/~amini/LICENSE.md'},
'VERSION': '0.13'
}


CRISPY_TEMPLATE_PACK = "bootstrap3"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 50,
    "DEFAULT_PERMISSION_CLASSES": (
        #"rest_framework.permissions.DjangoModelPermissions",
        #"rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
        # use IsAuthenticated for every logged in user to have global edit rights
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
       'url_filter.integrations.drf.DjangoFilterBackend',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
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
    "crum.CurrentRequestUserMiddleware",
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

APIS_BASE_URI = "https://sola.acdh-dev.oeaw.ac.at/apis/api/entity/"

APIS_MIN_CHAR = 3

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

APIS_BIBSONOMY_FIELDS = [
    # so that the whole entity can be used as well
    "self",
    # mutual fields between different entities
    "migne_number",
    # TempEntityClass fields
    "name",
    "start_date_written",
    "end_date_written",
    # Place fields
    "kind",
    # Publication fields
    "clavis_number",
]

APIS_BIBSONOMY_TEXTS = [
    # Person texts
    "Biographie (EN)",
    "Biographie (DE)",
    # Institution texts
    "Beschreibung (EN)",
    "Beschreibung (DE)",
    # Passage texts
    "Inhalt (ist zu übertragen zu publications)",
    "Übersetzung (EN)",
    "Übersetzung (DE)",
    "Originaltext / Zitat",
    "Auswertung (EN)",
    "Auswertung (DE)",
    # Publication texts
    "Inhalt (EN)",
    "Inhalt (DE)",
]

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
    "annotation_set_relation",
]

APIS_API_ADDITIONAL_FILTERS = {
    "Person": [
        ("publication_set__id", ["in", "exact"]),
        ("publication_relationtype_set__id", ["in", "exact"]),
        ("passage_set__id", ["in", "exact"]),
        ("passage_relationtype_set__id", ["in", "exact"]),
    ],
    "Passage": [
        ("person_set__id", ["in", "exact"]),
        ("person_relationtype_set__id", ["in", "exact"]),
        ("event_set__id", ["in", "exact"]),
        ("event_relationtype_set__id", ["in", "exact"]),
        ("publication_set__id", ["in", "exact"]),
        ("publication_set__person_set__id", ["in", "exact"]),
        ("publication_relationtype_set__id", ["in", "exact"]),
        ("publication_set__person_relationtype_set__id", ["in", "exact"]),
    ],
    "Event": [
        ("passage_set__id", ["in", "exact"]),
        ("passage_relationtype_set__id", ["in", "exact"]),
    ],
    "PassageType": [
        ("parent_class__id", ["in", "exact", "isnull"]),
    ],
}

APIS_RELATIONS = {
    "list_filters": [("relation_type",)],
    "search": ["relation_type__name"],
    "exclude": ["name"],
    "PersonPlace": {
        "labels": ["related_person", "related_place", "relation_type"],
        "search": [
            "relation_type__name",
            "related_person__name",
            "related_place__name",
        ],
        "list_filters": [("relation_type",), ("related_person",), ("related_place",)],
    },
    "PersonInstitution": {
        "labels": ["related_person", "related_institution", "relation_type"],
        "search": [
            "relation_type__name",
            "related_person__name",
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
            "related_event__name",
        ],
        "list_filters": [("relation_type",), ("related_person",), ("related_event",)],
    },
    "PersonPassage": {
        "labels": ["related_person", "related_passage", "relation_type"],
        "search": [
            "relation_type__name",
            "related_person__name",
            "related_passage__name",
        ],
        "list_filters": [("relation_type",), ("related_person",), ("related_passage",)],
    },
    "PersonPublication": {
        "labels": ["related_person", "related_publication", "relation_type"],
        "search": [
            "relation_type__name",
            "related_person__name",
            "related_publication__name",
        ],
        "list_filters": [
            ("relation_type",),
            ("related_person",),
            ("related_publication",),
        ],
    },
    "PersonPerson": {
        "labels": ["related_personA", "related_personB", "relation_type"],
        "search": [
            "relation_type__name",
            "related_personA__name",
            "related_personB__name",
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
    "InstitutionPassage": {
        "labels": ["related_institution", "related_passage", "relation_type"],
        "search": [
            "relation_type__name",
            "related_institution__name",
            "related_passage__name",
        ],
        "list_filters": [
            ("relation_type",),
            ("related_institution",),
            ("related_passage",),
        ],
    },
    "InstitutionPublication": {
        "labels": ["related_institution", "related_publication", "relation_type"],
        "search": [
            "relation_type__name",
            "related_institution__name",
            "related_publication__name",
        ],
        "list_filters": [
            ("relation_type",),
            ("related_institution",),
            ("related_publication",),
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
    "PlacePassage": {
        "labels": ["related_passage", "related_place", "relation_type"],
        "search": [
            "relation_type__name",
            "related_place__name",
            "related_passage__name",
        ],
        "list_filters": [("relation_type",), ("related_place",), ("related_passage",)],
    },
    "PlacePublication": {
        "labels": ["related_publication", "related_place", "relation_type"],
        "search": [
            "relation_type__name",
            "related_place__name",
            "related_publication__name",
        ],
        "list_filters": [
            ("relation_type",),
            ("related_place",),
            ("related_publication",),
        ],
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
    "EventPassage": {
        "labels": ["related_event", "related_passage", "relation_type"],
        "search": [
            "relation_type__name",
            "related_event__name",
            "related_passage__name",
        ],
        "list_filters": [("relation_type",), ("related_event",), ("related_passage",)],
    },
    "EventPublication": {
        "labels": ["related_event", "related_publication", "relation_type"],
        "search": [
            "relation_type__name",
            "related_event__name",
            "related_publication__name",
        ],
        "list_filters": [
            ("relation_type",),
            ("related_event",),
            ("related_publication",),
        ],
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
    "PassagePublication": {
        "labels": ["related_passage", "related_publication", "relation_type"],
        "search": [
            "relation_type__name",
            "related_passage__name",
            "related_publication__name",
        ],
        "list_filters": [
            ("relation_type",),
            ("related_passage",),
            ("related_publication",),
        ],
    },
    "PassagePassage": {
        "labels": ["related_passageA", "related_passageB", "relation_type"],
        "search": [
            "relation_type__name",
            "related_passageA__name",
            "related_passageB__name",
        ],
        "list_filters": [
            ("relation_type",),
            ("related_passageA",),
            ("related_passageB",),
        ],
    },
    "PublicationPublication": {
        "labels": ["related_publicationA", "related_publicationB", "relation_type"],
        "search": [
            "relation_type__name",
            "related_publicationA__name",
            "related_publicationB__name",
        ],
        "list_filters": [
            ("relation_type",),
            ("related_publicationA",),
            ("related_publicationB",),
        ],
    },
}

APIS_HIGHLIGHTER_ENTITIES = (
    "apis_entities.Person",
    "apis_entities.Institution",
    "apis_entities.Place",
    "apis_entities.Event",
    "apis_entities.Passage",
    "apis_entities.Publication",
    "apis_relations.PersonPerson",
    "apis_relations.PersonPlace",
    "apis_relations.PersonInstitution",
    "apis_relations.PersonEvent",
    "apis_relations.PersonPassage",
    "apis_relations.PersonPublication",
    "apis_relations.InstitutionPlace",
    "apis_relations.InstitutionEvent",
    "apis_relations.InstitutionPassage",
    "apis_relations.InstitutionPublication",
    "apis_relations.InstitutionInstitution",
    "apis_relations.PlaceEvent",
    "apis_relations.PlacePassage",
    "apis_relations.PlacePublication",
    "apis_relations.PlacePlace",
    "apis_relations.EventPassage",
    "apis_relations.EventPublication",
    "apis_relations.EventEvent",
    "apis_relations.PassagePublication",
    "apis_relations.PassagePassage",
    "apis_relations.PublicationPublication",
)

APIS_VOCABULARIES = {"exclude": ["userAdded"]}

APIS_METAINFO = {"exclude": ["groups_allowed"]}

APIS_ENTITIES = {
    "Place": {
        "merge": True,
        "search": ["name"],
        "form_order": ["name", "kind", "lat", "lng", "status", "collection"],
        "table_fields": ["name", "assigned_user"],
        "additional_cols": ["id", "lat", "lng", "part_of"],
        "list_filters": [
            {"name": {"method": "name_label_filter"}},
            {"collection": {"label": "Collection"}},
            {"kind": {"label": "Kind of Place"}},
            "assigned_user",
            "related_entity_name",
            "related_relationtype_name",
            "lat",
            "lng",
        ],
    },
    "Person": {
        "merge": True,
        "search": ["name"],
        "form_order": [
            "name",
            "gender",
            "start_date_written",
            "end_date_written",
            "status",
            "collection",
            "assigned_user",
        ],
        "table_fields": [
            "name",
            "assigned_user",
            "start_date_written",
            "end_date_written",
        ],
        "additional_cols": [
            "id",
            "gender",
        ],
        "list_filters": [
            "name",
            {"gender": {"label": "Gender"}},
            {"start_date": {"label": "Date of Birth"}},
            {"end_date": {"label": "Date of Death"}},
            {"title": {"label": "Title"}},
            {"collection": {"label": "Collection"}},
            "assigned_user",
            "related_entity_name",
            "related_relationtype_name",
        ],
    },
    "Institution": {
        "merge": True,
        "search": ["name"],
        "form_order": [
            "name",
            "name_english",
            "start_date_written",
            "end_date_written",
            "kind",
            "status",
            "collection",
            "assigned_user",
        ],
        "table_fields": ["name", "assigned_user"],
        "additional_cols": [
            "id",
            "kind",
        ],
        "list_filters": [
            {"name": {"label": "Name or label of institution"}},
            {"kind": {"label": "Kind of Institution"}},
            {"start_date": {"label": "Date of foundation"}},
            {"end_date": {"label": "Date of termination"}},
            {"collection": {"label": "Collection"}},
            "assigned_user",
            "related_entity_name",
            "related_relationtype_name",
        ],
    },
    "Passage": {
        "merge": True,
        "search": ["name"],
        "form_order": [
            "name",
            "start_date_written",
            "end_date_written",
            "kind",
            "status",
            "collection",
            "assigned_user",
        ],
        "table_fields": ["name", "assigned_user"],
        "additional_cols": [
            "id",
            "kind",
        ],
        "list_filters": [
            {"name": {"label": "Name of Passage"}},
            {"kind": {"label": "Kind of Passage"}},
            {"start_date": {"label": "Date of creation"}},
            {"end_date": {"label": "Date of termination"}},
            {"collection": {"label": "Collection"}},
            "assigned_user",
            "related_entity_name",
            "related_relationtype_name",
        ],
    },
    "Publication": {
        "merge": True,
        "search": ["name"],
        "form_order": [
            "name",
            "start_date_written",
            "end_date_written",
            "kind",
            "status",
            "collection",
            "assigned_user",
        ],
        "table_fields": ["name", "assigned_user"],
        "additional_cols": [
            "id",
            "kind",
        ],
        "list_filters": [
            {"name": {"label": "Name of publication"}},
            {"kind": {"label": "Kind of publication"}},
            {"start_date": {"label": "Date of creation"}},
            {"collection": {"label": "Collection"}},
            "assigned_user",
            "related_entity_name",
            "related_relationtype_name",
        ],
    },
    "Event": {
        "merge": True,
        "search": ["name"],
        "form_order": [
            "name",
            "name_english",
            "start_date_written",
            "end_date_written",
            "kind",
            "status",
            "collection",
            "assigned_user",
        ],
        "table_fields": ["name", "assigned_user"],
        "additional_cols": [
            "id",
        ],
        "list_filters": [
            {"name": {"label": "Name of event"}},
            {"kind": {"label": "Kind of Event"}},
            {"start_date": {"label": "Date of beginning"}},
            {"end_date": {"label": "Date of end"}},
            {"collection": {"label": "Collection"}},
            "assigned_user",
            "related_entity_name",
            "related_relationtype_name",
        ],
    },
}

APIS_API_EXCLUDE_SETS = True  # exclude reverse links to entities

APIS_LIST_VIEWS_ALLOWED = False
APIS_DETAIL_VIEWS_ALLOWED = False
MAX_AGE = 60 * 60

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

SUMMERNOTE_CONFIG = {
    "summernote": {
        # As an example, using Summernote Air-mode
        "airMode": False,
        # Change editor size
        "width": "100%",
        "height": "400",
        # Use proper language setting automatically (default)
        "lang": None,
        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        "toolbar": [
            ["style", ["style"]],
            ["font", ["bold", "underline", "italic"]],
            ["color", ["color"]],
            ["para", ["ul", "ol", "paragraph"]],
            ["view", ["fullscreen"]],
        ],
    }
}
