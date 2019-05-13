from django.conf import settings
from django.conf.urls import handler404, include, url
from django.contrib import admin
from django.db.utils import ProgrammingError
from rest_framework import routers

urlpatterns = [
    url(r"^bibsonomy/", include("apis_bibsonomy.urls", namespace="bibsonomy")),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^admin/", admin.site.urls),
    url(r"^", include("webpage.urls", namespace="webpage")),
]
try:
    urlpatterns.append(url(r"^apis/", include("apis_core.urls", namespace="apis")))
except ProgrammingError:
    print(
        "content types not found, skipping. Please note, apis has not been added to your app yet."
    )

handler404 = "webpage.views.handler404"
