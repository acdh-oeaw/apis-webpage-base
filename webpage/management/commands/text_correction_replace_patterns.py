import re
import csv
from django.core.management.base import BaseCommand, CommandError
from apis_core.apis_metainfo.models import Text

class Command(BaseCommand):

    def handle(self, *args, **options):


        def clean_text_additional(t):

            t = re.sub(r"<a href.*?>|</a>", "", t, flags=re.DOTALL)
            t = re.sub(r"<a name=.*?>|</a>", "", t, flags=re.DOTALL)
            t = re.sub(r"<a style=.*?>|</a>", "", t, flags=re.DOTALL)
            t = re.sub(r"<b style=.*?>|</a>", "", t, flags=re.DOTALL)
            t = re.sub(r"<font face=.*?>|</font>", "", t, flags=re.DOTALL)
            t = re.sub(r"<sup>|</sup>", "", t, flags=re.DOTALL)
            t = re.sub(r"<i>|</i>", "", t, flags=re.DOTALL)
            t = re.sub(r"<b>|</b>", "", t, flags=re.DOTALL)
            t = re.sub(r"<o:p>|</o:p>", "", t, flags=re.DOTALL)
            t = re.sub(r"<i style.*?>", "", t, flags=re.DOTALL)
            t = re.sub(r"<h[0-9]+.*?>|</h.*?>", "", t, flags=re.DOTALL)
            t = re.sub(r"<br .*?>", "", t, flags=re.DOTALL)
            t = re.sub(r"&nbsp;", "", t, flags=re.DOTALL)

            return t


        def read_from_csv():

            with open("patterns.csv", "r") as f:

                patterns_dict_list = csv.DictReader(f)

                return [pattern_dict for pattern_dict in patterns_dict_list]


        def main():

                patterns_dict_list = read_from_csv()
                cy = 0
                cn = 0

                for t in Text.objects.all():

                    text_old = t.text
                    text_new = clean_text_additional(text_old)

                    if text_new != text_old:
                        cy += 1

                        # print("-----------------------------------")
                        # print("-----------------------------------")
                        # print("text_old:\n", text_old)
                        # print("-----------------------------------")
                        # print("text_new:\n", text_new)
                        # print("-----------------------------------")
                        # print("-----------------------------------")

                    else:
                        cn += 1


                    for patterns_dict in patterns_dict_list:

                        pattern_incorrect = patterns_dict["pattern_incorrect"]
                        pattern_correct = patterns_dict["pattern_correct"]

                        pattern_check_incorrect = pattern_incorrect.replace("\n", "")
                        pattern_check_correct = pattern_correct.replace("\n", "")

                        if (
                            pattern_check_incorrect.isspace()
                            or pattern_check_incorrect == ""
                            or pattern_check_correct == pattern_check_incorrect
                            or pattern_check_correct.startswith(" ")
                            or pattern_check_correct.endswith(" ")
                            or pattern_check_incorrect == "nachdem"
                            or pattern_incorrect == "authority).\n\nThe"
                            or pattern_incorrect == "interpretable.\n\nThis"
                        ):
                            continue

                        else:
                            text_new_new = text_new.replace(pattern_incorrect, pattern_correct)

                            if text_new_new != text_new:

                                print("-----------------------------------")
                                print("-----------------------------------")
                                print("text_new:\n", text_new)
                                print("-----------------------------------")
                                print("text_new_new:\n", text_new_new)
                                print("-----------------------------------")
                                print("-----------------------------------")
                                print("pattern_incorrect:", pattern_incorrect)
                                print("pattern_correct:", pattern_correct)
                                print()

                            text_new = text_new_new

                    t.text = text_new

                    t.save()


                print("cy:", cy)
                print("cn:", cn)


        main()