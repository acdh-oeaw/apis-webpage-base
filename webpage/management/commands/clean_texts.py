import re
from django.core.management.base import BaseCommand, CommandError
from apis_core.apis_metainfo.models import Text

class Command(BaseCommand):

    def handle(self, *args, **options):

        def clean_text(t):

            t = re.sub(r"<!--\[if gte.*?endif\]-->", "", t, flags=re.DOTALL)
            t = re.sub(r"<p.*?>", "", t, flags=re.DOTALL)
            t = re.sub(r"<span.*?>|</span>", "", t, flags=re.DOTALL)
            t = re.sub(r"\r\n", "", t, flags=re.DOTALL)
            t = re.sub(r"<br>", "", t, flags=re.DOTALL)
            t = re.sub(r"<div.*?>|</div>", "", t, flags=re.DOTALL)
            t = re.sub(r"</p>", "\n\n", t, flags=re.DOTALL)

            return t

        for t in Text.objects.all():

            t.text = clean_text(t.text)
            t.save()