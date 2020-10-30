from django.core.management.base import BaseCommand, CommandError
from apis_core.apis_metainfo.models import Text

class Command(BaseCommand):

    def handle(self, *args, **options):

        def replace_nl(t):

            if t is not None and t != "":
                t = t.replace("\r", "")
                t = t.split("\n")
                t = ["<p>" + x + "</p>" for x in t]
                t = "".join(t)

            return t


        for t in Text.objects.all():

            t.text = replace_nl(t.text)

            t.save()
