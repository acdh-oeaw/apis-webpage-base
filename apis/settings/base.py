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
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, '../'))))

# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reversion',
    'reversion_compare',
    'crispy_forms',
    'django_filters',
    'django_tables2',
    'rest_framework',
    'webpage',
    'browsing',
    'stats',
    'django_extensions',
    'apis_core.apis_entities',
    'apis_core.apis_metainfo',
    'apis_core.apis_relations',
    'apis_core.apis_vocabularies',
    'apis_core.apis_labels',
    'apis_core.apis_vis',
    'rest_framework.authtoken',
    'guardian',
    'charts',
]

CRISPY_TEMPLATE_PACK = "bootstrap3"

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50,
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )

}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # this is default
    'guardian.backends.ObjectPermissionBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
]

ROOT_URLCONF = 'apis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'webpage.webpage_content_processors.installed_apps',
                'webpage.webpage_content_processors.is_dev_version',
                'webpage.webpage_content_processors.get_db_name',
                'apis_core.context_processors.custom_context_processors.add_entities',
                'apis_core.context_processors.custom_context_processors.add_relations',
                'apis_core.context_processors.custom_context_processors.add_apis_settings',

            ],
        },
    },
]

WSGI_APPLICATION = 'apis.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

APIS_BASE_URI = 'TO CHANGE'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

APIS_COMPONENTS = []
# APIS settings

APIS_TEI_TEXTS = ['xml/tei transcription']
APIS_CETEICEAN_CSS = "https://teic.github.io/CETEIcean/css/CETEIcean.css"
APIS_CETEICEAN_JS = "https://teic.github.io/CETEIcean/js/CETEI.js"

APIS_NEXT_PREV = True

APIS_ALTERNATE_NAMES = [
    'Taufname',
    'Ehename',
    'Name laut ÖBL XML',
    'alternative Namensform',
    'alternative name',
    'Künstlername',
    'Mädchenname',
    'Pseudonym',
    'weitere Namensform'
  ]

APIS_RELATIONS_FILTER_EXCLUDE = [
    'uri',
    'tempentityclass',
    'user', '__id',
    'source',
    'label',
    'temp_entity',
    'collection__',
    '_ptr',
    'baseclass',
    'id',
    'written',
    'relation_type__description',
    'relation_type__parent_class',
    'relation_type__status',
    'relation_type__vocab_name',
    'relation_type__name_reverse',
    '__text',
]

APIS_RELATIONS = {
    'PersonPlace': {
        'exclude': ['name']
    }
}


APIS_ENTITIES = {
    'Place': {
        'search': ['name'],
        'table_fields': [
            'name',
        ],
        'additional_cols': [
            'lat', 'lng', 'part_of'
        ],
        'list_filters': [
            ('name', {'method': 'wildcard_filter', 'label': 'Name'}),
            ('status', {'method': 'wildcard_filter', 'label': 'Status'}),
            ('collection', {'label': 'Collection'})
        ]
    },
    'Person': {
        'merge': True,
        'search': ['name', 'first_name'],
        'form_order': ['first_name', 'name'],
        'table_fields': ['name', 'first_name', 'start_date', 'end_date'],
        'additional_cols': [
                   'profession', 'gender',
           ],
        'list_filters': [
            ('name', {'method': 'name_label_filter', 'label': 'Name complete'}),
            ('first_name', {'method': 'wildcard_filter', 'label': 'Firstname'}),
            ('gender', {'label': 'Gender'}),
            ('start_date', {'label': 'Date of Birth'}),
            ('end_date', {'label': 'Date of Death'}),
            # TODO __sresch__ remove
            # ('profession', {'label': 'Profession'}),
            ('collection', {'label': 'Collection'})
        ]
    },
    'Institution': {
        'search': ['name'],
        'list_filters': [
            ('name', {'method': 'wildcard_filter', 'label': 'Name'}),
            ('start_date', {'label': 'Date of foundation'}),
            ('end_date', {'label': 'Date of termination'}),
            ('collection', {'label': 'Collection'})
        ]
    },
    'Passage': {
        'search': ['name'],
        'list_filters': [
            ('name', {'method': 'wildcard_filter', 'label': 'Name'})
        ]
    },
    'Publication': {
        'search': ['name'],
        'list_filters': [
            ('name', {'method': 'wildcard_filter', 'label': 'Name'})
        ]
    },
    'Event': {
        'search': ['name'],
        'list_filters': [
            ('name', {'method': 'wildcard_filter', 'label': 'Name'})
        ]
    },
}


APIS_LIST_VIEWS_ALLOWED = False
APIS_DETAIL_VIEWS_ALLOWED = False

APIS_LIST_VIEW_TEMPLATE = "browsing/generic_list.html"
APIS_DELETE_VIEW_TEMPLATE = "webpage/confirm_delete.html"


PROJECTS = {
    'STB':
        {
            'abbr': 'STB',
            'title': 'Schnitzler Diary',
            'resolver_person': 'pages/person-detail.html?personID=',
            'resolver_place': 'pages/place-detail.html?placeID=',
            'base_url': 'https://dse.hephaistos.arz.oeaw.ac.at/exist/apps/schnitzler-process',
        },
    'HBAS':
        {
            'abbr': 'HBAS',
            'title': 'Die Korrespondenz Hermann Bahr – Arthur Schnitzler',
            'resolver_person': 'register.html?key=',
            'resolver_place': 'register.html?key=',
            'base_url': 'https://bahrschnitzler.acdh.oeaw.ac.at'
        },
    'FK':
        {
            'abbr': 'FK',
            'title': 'Die Fackel',
            'resolver_person': 'pages/person-detail.html?personID=',
            'resolver_place': 'pages/place-detail.html?placeID=',
            'base_url': 'https://fackel.acdh.oeaw.ac.at',
        },
    'BR':
        {
            'abbr': 'Brenner',
            'title': 'Der Brenner',
            'resolver_person': 'pages/person-detail.html?personID=',
            'resolver_place': 'pages/place-detail.html?placeID=',
            'base_url': 'https://brenner.acdh.oeaw.ac.at',
        },
    'ASBW':
        {
            'abbr': 'ASBW',
            'title': 'Arthur Schnitzler Briefwechsel mit Autorinnen und Autoren',
            'resolver_person': 'register.html?key=',
            'resolver_place': 'register.html?key=',
            'base_url': 'https://schnitzler-briefe.acdh.oeaw.ac.at'
        },
}

APIS_IIIF_WORK_KIND = 'IIIF'
APIS_IIIF_ENT_IIIF_REL = "has iiif image"
APIS_IIIF_SERVER = "https://iiif.acdh.oeaw.ac.at/"
# APIS_OPENSEADRAGON_CSS = "https://teic.github.io/CETEIcean/css/CETEIcean.css"
APIS_OSD_JS = "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/2.4.0/openseadragon.min.js"
APIS_OSD_IMG_PREFIX = "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/2.4.0/images/"
