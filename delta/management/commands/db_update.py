from django.core.management.base import BaseCommand, CommandError
from delta.models import DiningLocation, MealPeriod, MenuItem

import requests
import xml.etree.ElementTree as ElemTree
import datetime
import base64

class Command(BaseCommand):
    help = "Pulls menu data from Cal Dining"

    def pull_data(self, payload, url):
        try:
            res = requests.post(url, payload).text.replace("&", "and")
            tree = ElemTree.fromstring(res)
            return tree
        except ElemTree.ParseError:
            self.stdout.write("WARNING: malformed XML input data")
            return

    def build_data(self, payload, dining_location, tree):
        # location = DiningLocation.objects.get(location=payload["location"])
        self.stdout.write(f"{payload} {tree}")
        for mp in tree[0][1][1]:
            mp_name = mp[0].text
            mp_uid_ascii = f"{dining_location.location}_{mp_name}_{str(datetime.date.today())}".encode("ascii")
            mp_uid_b64 = base64.b64encode(mp_uid_ascii)
            mp_uid_b64_str = mp_uid_b64.decode("ascii")
            if not MealPeriod.objects.filter(uid=mp_uid_b64_str):
                mp_row = MealPeriod(location=dining_location, uid=mp_uid_b64_str, period=mp_name, date=datetime.date.today())
                mp_row.save()
            else:
                continue
            self.stdout.write(f"{mp_name} {mp_row}") # stdout: Breakfast - Spring, Lunch - Spring ...
            meal_period_categories = mp[1]

            for category in meal_period_categories:
                category_name = category[0].text
                self.stdout.write(category_name) # stdout: BREAKFAST MENU, HOT CEREALS ...
                food_items = category[1]

                for food_item in food_items:
                    item_name = food_item[0].text
                    advisories = food_item[1]
                    uid_ascii = f"{payload['date']}_{dining_location.location}_{mp_name}_{item_name}".encode("ascii")
                    uid_b64 = base64.b64encode(uid_ascii)
                    uid_b64_str = uid_b64.decode("ascii")
                    if not MenuItem.objects.filter(uid=uid_b64_str):
                        item_row = MenuItem(meal_period=mp_row, uid=uid_b64_str, name=item_name, category=category_name)
                        item_row.save()
                    else:
                        continue
                    self.stdout.write(f"{item_name} {[advisories[i][1].text for i in range(len(advisories))]} {item_row}")

        self.stdout.write("\n")

    def handle(self, *args, **options):
        url = "https://caldining.berkeley.edu/wp-admin/admin-ajax.php"

        all_dining_locations = [location for location in DiningLocation.objects.all()]

        payloads = [
            {
                "action": "cald_filter_xml",
                "location": location.location.replace(" ", "_"),
                "mealperiod": None,
                "date": int(str(datetime.date.today()).replace("-", "")),
            }
            for location in all_dining_locations
        ]

        for dining_location, payload in zip(all_dining_locations, payloads):
            raw_elem_tree = self.pull_data(payload, url)
            self.build_data(payload, dining_location, raw_elem_tree)

        self.stdout.write("Pull data operation completed.")