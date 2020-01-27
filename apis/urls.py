from django.conf.urls import url, include, handler404
from django.contrib import admin
from django.conf import settings
from rest_framework import routers


if 'theme' in settings.INSTALLED_APPS:
    urlpatterns = [
        url(r'^apis/', include('apis_core.urls', namespace="apis")),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^admin/', admin.site.urls),
        url(r'^info/', include('infos.urls', namespace='info')),
        url(r'^bibsonomy/', include('apis_bibsonomy.urls', namespace="bibsonomy")),
        url(r'^', include('theme.urls', namespace='theme')),
        url(r'^webpage/', include('webpage.urls', namespace='webpage')),
    ]
else:
    urlpatterns = [
        url(r'^apis/', include('apis_core.urls', namespace="apis")),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^admin/', admin.site.urls),
        url(r'^info/', include('infos.urls', namespace='info')),
        url(r'^bibsonomy/', include('apis_bibsonomy.urls', namespace="bibsonomy")),
        url(r'^', include('webpage.urls', namespace='webpage')),
    ]


handler404 = 'webpage.views.handler404'
