# EL NEW:
from django.core.management.base import BaseCommand
from apis_highlighter.models import Annotation


class Command(BaseCommand):

    def handle(self, *args, **options):

        def migrate():

            qs = Annotation.objects.all()
            print(f"Migrating {len(qs)} annotations.")

            for a in qs:
                if len(a.entity_link.all()) > 1:
                    raise Exception("A highlight has been found to be related to more than 1 other model! Aborting.")

            for a in qs:
                rel_qs = a.entity_link.all()
                if len(rel_qs) == 1:
                    rel_model = rel_qs[0]
                    a.entity_link_new = rel_model
                    a.save()
            print("done")

        def check():

            print("Checking correspondence between old and new annotations.")
            for a in Annotation.objects.all():
                if a.entity_link_new is not None or len(a.entity_link.all()) == 1:
                    if a.entity_link_new != a.entity_link.all()[0]:
                        raise Exception(f"Discrepancy found on annotation {a}! Aborting.")
            print("done")

        def delete():

            print("Deleting old annotations.")
            for a in Annotation.objects.all():
                a.entity_link.clear()
            print("done")

        migrate()
        check()
        delete()
