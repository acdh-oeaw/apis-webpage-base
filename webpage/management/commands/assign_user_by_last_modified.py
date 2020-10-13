from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from apis_core.apis_entities.models import AbstractEntity
from apis_core.apis_metainfo.models import TempEntityClass
from reversion.models import Version

class Command(BaseCommand):

    def handle(self, *args, **options):

        usernames_to_exlude = ["SResch", "DSchopper", "sennierer", "acdh", "sprobst", "client", "AnonymousUser"]
        user_anon = User.objects.get(username="AnonymousUser")

        user_qs_to_exclude = User.objects.filter(username__in=usernames_to_exlude)

        print("User set not to be assigned:", user_qs_to_exclude)
        print("User set to be assigned:",  User.objects.exclude(username__in=usernames_to_exlude))

        for entity_class in AbstractEntity.get_all_entity_classes():

            for e in entity_class.objects.all():

                v_qs = Version.objects.get_for_object(e)

                v_qs = v_qs.exclude(revision__user__in=user_qs_to_exclude)

                v_qs = v_qs.order_by("-revision__date_created")

                v = v_qs.first()

                if v is not None:
                    user = v.revision.user
                    date = v.revision.date_created
                else:
                    user = user_anon
                    date = None

                e.assigned_user = user

                e.save()

                print(
                    "-------- Assigned User:\n"
                    f"to {e.__class__.__name__}: {e}\n"
                    f"user: {user}\n"
                    f"due to last modification date: {date}\n"
                )

