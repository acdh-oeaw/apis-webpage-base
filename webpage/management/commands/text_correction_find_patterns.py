import re
import csv
from django.core.management.base import BaseCommand, CommandError
from apis_core.apis_metainfo.models import Text

class Command(BaseCommand):

    def handle(self, *args, **options):

        def clean_text_without_r_n(t):
            t = re.sub(r"<!--\[if gte.*?endif\]-->", "", t, flags=re.DOTALL)
            t = re.sub(r"<p.*?>", "", t, flags=re.DOTALL)
            t = re.sub(r"<span.*?>|</span>", "", t, flags=re.DOTALL)
            # t = re.sub(r"\r\n", "", t, flags=re.DOTALL)
            t = re.sub(r"<br>", "", t, flags=re.DOTALL)
            t = re.sub(r"<div.*?>|</div>", "", t, flags=re.DOTALL)
            t = re.sub(r"</p>", "\n\n", t, flags=re.DOTALL)

            return t

        def clean_text_additional(t):
            t = re.sub(r"<a.*?>|</a>", "", t, flags=re.DOTALL)
            t = re.sub(r"<i>|</i>", "", t, flags=re.DOTALL)
            t = re.sub(r"<b>|</b>", "", t, flags=re.DOTALL)
            t = re.sub(r"<o:p>|</o:p>", "", t, flags=re.DOTALL)
            t = re.sub(r"<i style.*?>", "", t, flags=re.DOTALL)
            t = re.sub(r"<h[0-9]+.*?>|</h.*?>", "", t, flags=re.DOTALL)
            t = re.sub(r"<br .*?>", "", t, flags=re.DOTALL)
            t = re.sub(r"&nbsp;", " ", t, flags=re.DOTALL)

            return t


        def get_patterns(t, pattern):

            patterns_unmodified = re.findall(f"[^ ]+{pattern}[^ ]+", t)
            patterns_incorrect = []
            patterns_correct = []

            for tt in patterns_unmodified:

                patterns_incorrect.append(re.sub(pattern, "", tt, flags=re.DOTALL))
                patterns_correct.append(re.sub(pattern, " ", tt, flags=re.DOTALL))

            return [
                (pf, pi, pc)
                for pf, pi, pc
                in zip(patterns_unmodified, patterns_incorrect, patterns_correct)
            ]


        def write_to_csv(all_patterns_set):

            all_patterns_list_sorted = list(all_patterns_set)
            all_patterns_list_sorted.sort()

            with open("patterns.csv", "w") as f:

                w = csv.writer(f)
                w.writerow(["pattern_unmodified", "pattern_incorrect", "pattern_correct"])
                for pattern in all_patterns_list_sorted:
                    w.writerow(pattern)

        def main():

            all_patterns_list = []

            for t in Text.objects.all():

                t_pk = t.pk
                t=t.text

                t = clean_text_without_r_n(t)
                t = clean_text_additional(t)

                t_check = t.replace("\n", "").replace("\r", "")
                if t_check.isspace() or t_check == "":
                    continue

                all_patterns_list.extend(get_patterns(t, "\\r\\n"))
                all_patterns_list.extend(get_patterns(t, "<br>"))

            all_patterns_set = set(all_patterns_list)

            write_to_csv(all_patterns_set)


        main()