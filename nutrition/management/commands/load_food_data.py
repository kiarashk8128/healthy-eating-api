import csv
from django.core.management.base import BaseCommand
from nutrition.models import FoodGroup, Food, ServingPerDay, DirectionalStatement


class Command(BaseCommand):
    help = 'Load food data into the database'

    def handle(self, *args, **options):
        self.load_food_groups()
        self.load_foods()
        self.load_servings_per_day()
        self.load_directional_statements()

    def load_food_groups(self):
        with open('data/foodgroups-en_ONPP.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                FoodGroup.objects.update_or_create(
                    fgcat_id=row['fgcat_id'],
                    defaults={
                        'fgid': row['fgid'],
                        'fgcat': row['fgcat'],
                        'foodgroup': row['foodgroup'],
                    }
                )

    def load_foods(self):
        with open('data/foods-en_ONPP_rev.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Get the FoodGroup instance by fgcat_id
                food_group = FoodGroup.objects.get(fgcat_id=row['fgcat_id'])
                # Now, create or update the Food object
                Food.objects.update_or_create(
                    food=row['food'],
                    defaults={
                        'fgid': row['fgid'],
                        'fgcat_id': food_group,  # Assign the FoodGroup instance
                        'srvg_sz': row['srvg_sz'],
                    }
                )

    def load_servings_per_day(self):
        with open('data/servings_per_day-en_ONPP.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ServingPerDay.objects.update_or_create(
                    gender=row['gender'],
                    ages=row['ages'],
                    defaults={
                        'fgid': row['fgid'],
                        'servings': row['servings'],
                    }
                )

    def load_directional_statements(self):
        with open('data/fg_directional_satements-en_ONPP.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                DirectionalStatement.objects.update_or_create(
                    fgid=row['fgid'],
                    defaults={
                        'directional_statement': row['directional-statement'],
                    }
                )
