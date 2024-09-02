import random
from datetime import date

from nutrition.models import FoodGroup, Food, ServingPerDay, Menu


def calculate_age(birthdate):
    """Calculate age based on the birthdate."""
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def get_serving_requirements(user_or_member):
    """Get the serving requirements based on gender and calculated age."""
    gender = user_or_member.gender
    age = calculate_age(user_or_member.birthday)  # Calculate age from birthdate
    age_group = get_age_group(age)
    serving_requirements = ServingPerDay.objects.filter(gender=gender, ages=age_group)
    return serving_requirements


def get_age_group(age):
    """Determine the age group for a given age."""
    if 2 <= age <= 3:
        return '2 to 3'
    elif 4 <= age <= 8:
        return '4 to 8'
    elif 9 <= age <= 13:
        return '9 to 13'
    elif 14 <= age <= 18:
        return '14 to 18'
    elif 19 <= age <= 30:
        return '19 to 30'
    elif 31 <= age <= 50:
        return '31 to 50'
    elif 51 <= age <= 70:
        return '51 to 70'
    else:
        return '71+'


def apply_directional_statements(menu):
    """Apply directional statements to modify the menu."""
    for day, meals in menu.items():
        apply_dark_green_and_orange_veg(meals)
        apply_limited_fat_sugar_salt_vf(meals)
        apply_low_fat_sugar_salt_grains(meals)
        apply_mi_statements(meals)
    ensure_meat_guidelines_across_week(menu)


def apply_dark_green_and_orange_veg(meals):
    """Ensure at least one dark green and one orange vegetable each day."""
    dark_green_veg_food = Food.objects.filter(fgcat_id=2).order_by('?').first()
    meals.append({
        'food_group': 'Vegetables and Fruit',
        'food_item': dark_green_veg_food.food,
        'serving_size': dark_green_veg_food.srvg_sz,
    })
    orange_veg_food = Food.objects.filter(fgcat_id=3).order_by('?').first()
    meals.append({
        'food_group': 'Vegetables and Fruit',
        'food_item': orange_veg_food.food,
        'serving_size': orange_veg_food.srvg_sz,
    })


def apply_more_veg_than_juice(menu):
    all_meals = []
    for meals in menu.values():
        all_meals.extend(meals)

    """Ensure vegetables and fruit are consumed more often than juice."""
    juice_items = [item for item in all_meals if 'juice' in item['food_item'].lower()]
    non_juice_items = [item for item in all_meals if 'juice' not in item['food_item'].lower()]

    if len(juice_items) >= len(non_juice_items):
        for juice_food in juice_items:
            all_meals.remove(juice_food)

            # Adjust the query to include fgcat_id 1, 2, and 3
            non_juice_food = Food.objects.filter(fgcat_id__in=[1, 2, 3]).exclude(food__icontains='juice').order_by(
                '?').first()

            if non_juice_food:
                all_meals.append({
                    'food_group': 'Vegetables and Fruit',
                    'food_item': non_juice_food.food,
                    'serving_size': non_juice_food.srvg_sz,
                })


def apply_limited_fat_sugar_salt_vf(meals):
    """Choose vegetables and fruit prepared with little or no added fat, sugar, or salt."""
    # List of vegetables and fruits that are typically low in added fat, sugar, and salt
    suitable_items = [
        'Asparagus', 'Green beans', 'Bok choy/Chinese cabbage (Choi sum)', 'Broccoli', 'Brussels sprouts', 'Carrots',
        'Chard', 'Dandelion greens', 'Endive', 'Fiddleheads', 'Kale/collards', 'Leeks', 'Romaine lettuce',
        'Mesclun mix', 'Mustard greens', 'Okra', 'Peas', 'Seaweed', 'Snow peas', 'Spinach', 'Zucchini',
        'Sweet green peppers', 'Edemame (soy beans)', 'Apple', 'Banana', 'Berries', 'Grapes', 'Kiwi',
        'Orange', 'Peach', 'Pear', 'Plum'
    ]

    # Check if any suitable item exists in the meals
    exists = any(item['food_item'] in suitable_items for item in meals)
    # If no suitable item exists, add one randomly
    if not exists:
        random_suitable_item = random.choice(suitable_items)
        selected_food = Food.objects.filter(food=random_suitable_item).first()
        meals.append({
            'food_group': 'Vegetables and Fruit',
            'food_item': selected_food.food,
            'serving_size': selected_food.srvg_sz,
        })


def apply_whole_grain_requirement(meals):
    """Ensure at least half of the grain products are whole grain by replacing non-whole grain items if necessary."""

    total_grains = [item for item in meals if item['food_group'] == 'Grains']

    whole_grains_in_meals = [item for item in total_grains if
                             item['food_item'] in Food.objects.filter(fgcat_id=5).values_list('food', flat=True)]

    non_whole_grains_in_meals = [item for item in total_grains if
                                 item['food_item'] not in Food.objects.filter(fgcat_id=5).values_list('food',
                                                                                                      flat=True)]

    # If less than half of the grains are whole grain, replace non-whole grains with whole grains
    if len(whole_grains_in_meals) < len(total_grains) / 2:
        missing_whole_grains = int(len(total_grains) / 2) - len(whole_grains_in_meals)

        for i in range(min(missing_whole_grains, len(non_whole_grains_in_meals))):
            whole_grain_food = Food.objects.filter(fgcat_id=5).order_by('?').first()

            # Replace a non-whole grain with a whole grain
            index_to_replace = meals.index(non_whole_grains_in_meals[i])
            meals[index_to_replace] = {
                'food_group': 'Grains',
                'food_item': whole_grain_food.food,
                'serving_size': whole_grain_food.srvg_sz,
            }


def apply_low_fat_sugar_salt_grains(meals):
    """Ensure grain products are lower in fat, sugar, or salt."""

    total_grains = [item for item in meals if item['food_group'] == 'Grains']

    low_fat_sugar_salt_grains = [
        'Cold cereal(whole grain)', 'Hot cereal(whole grain (example: oatmeal))', 'Rye crackers',
        'Muffin(whole grain)', 'Quinoa', 'Brown rice', 'Pasta/noodles(whole grain)',
        'Pita(whole wheat)', 'Tortilla(whole wheat)', 'Crackers(whole wheat)',
        'Wild rice', 'Roll(whole wheat)', 'Couscous(whole wheat)',
        'Popcorn(without added fat or salt)', 'English muffin(whole grain)'
    ]
    low_fat_sugar_salt_in_meals = [item for item in total_grains if item['food_item'] in low_fat_sugar_salt_grains]

    if not low_fat_sugar_salt_in_meals:
        low_fat_sugar_salt_food = Food.objects.filter(
            fgcat_id=5, food__in=low_fat_sugar_salt_grains
        ).order_by('?').first()
        meals.append({
            'food_group': 'Grains',
            'food_item': low_fat_sugar_salt_food.food,
            'serving_size': low_fat_sugar_salt_food.srvg_sz,
        })


def apply_mi_statements(meals):
    """Ensure that meals include skim, 1%, or 2% milk each day and select lower-fat milk alternatives."""

    # Identify all milk and milk alternatives in the meals
    milk_items = [item for item in meals if item['food_group'] == 'Milk and Alternatives']

    # Ensure there's at least one low-fat milk option (1%, 2%, skim)
    low_fat_milk_in_meals = [item for item in milk_items if item['food_item'] in [
        "Milk(1%, 2% skim)"
    ]]

    if not low_fat_milk_in_meals:
        low_fat_milk = Food.objects.filter(food="Milk(1%, 2% skim)").first()
        if low_fat_milk:
            meals.append({
                'food_group': 'Milk and Alternatives',
                'food_item': low_fat_milk.food,
                'serving_size': low_fat_milk.srvg_sz,
            })

    # Ensure there's at least one lower-fat milk alternative in the meals
    low_fat_milk_alternatives_in_meals = [item for item in milk_items if item['food_item'] in [
        "Fortified soy beverage (unsweetened)", "Cheese (cottage or quark)", "Goat Cheese", "Paneer", "Plain yogurt",
        "Kefir"
    ]]

    if not low_fat_milk_alternatives_in_meals:
        low_fat_milk_alternative = Food.objects.filter(food__in=[
            "Fortified soy beverage (unsweetened)", "Cheese (cottage or quark)", "Goat Cheese",
            "Paneer", "Plain yogurt", "Kefir"
        ]).order_by('?').first()

        if low_fat_milk_alternative:
            meals.append({
                'food_group': 'Milk and Alternatives',
                'food_item': low_fat_milk_alternative.food,
                'serving_size': low_fat_milk_alternative.srvg_sz,
            })


def ensure_meat_guidelines_across_week(menu):
    """Ensure that the weekly menu meets the guidelines for meat and alternatives."""

    # Options for each guideline
    meat_alternatives = [
        "Beans(cooked, canned)",
        "Lentils",
        "Tofu",
        "Eggs",
        "Nuts(shelled)",
        "Peanut butter or nut butters",
        "Seeds(shelled)"
    ]

    fish_options = [
        "Fish and shellfish(canned (example: crab or salmon or tuna))",
        "Fish(fresh or frozen (example: herring, mackerel, trout, salmon, sardines, squid, tuna))",
        "Shellfish(fresh or frozen (example: clams, crab, lobster, mussels, scallops, shrimp, prawns))"
    ]

    lean_meats = [
        "Deli meat(low-fat, lower sodium)",
        "Chicken",
        "Turkey",
        "Game meats (example: deer, moose, caribou, elk)",
        "Game birds (example: ptarmigan, partridge, grouse, goose)",
        "Bison/Buffalo",
        "Veal"
    ]
    meat_alternatives_count = 0
    fish_count = 0
    lean_meat_count = 0

    def find_day_with_least_meat():
        meat_counts = dict()
        for day, meals in menu.items():
            meat_counts[day] = sum(1 for item in meals if item['food_group'] == 'Meat and Alternatives')
        min_count = min(meat_counts.values())
        days_with_min_count = [day for day, count in meat_counts.items() if count == min_count]
        return random.choice(days_with_min_count)

    # Ensure meat alternatives are included often (e.g., at least three times a week)
    for meals in menu.values():
        meat_alternatives_count = sum(1 for item in meals if item['food_item'] in meat_alternatives)
    while meat_alternatives_count < 3:
        alternative_food = Food.objects.filter(food__in=meat_alternatives).order_by('?').first()
        if alternative_food:
            least_meat_day = find_day_with_least_meat()
            menu[least_meat_day].append({
                'food_group': 'Meat and Alternatives',
                'food_item': alternative_food.food,
                'serving_size': alternative_food.srvg_sz,
            })
            meat_alternatives_count += 1

    # Ensure at least two servings of fish are included each week
    for meals in menu.values():
        fish_count = sum(1 for item in meals if item['food_item'] in fish_options)
    while fish_count < 2:
        fish_food = Food.objects.filter(food__in=fish_options).order_by('?').first()
        if fish_food:
            least_meat_day = find_day_with_least_meat()
            menu[least_meat_day].append({
                'food_group': 'Meat and Alternatives',
                'food_item': fish_food.food,
                'serving_size': fish_food.srvg_sz,
            })
            fish_count += 1

    # Ensure lean meat and alternatives are included (at least once a week)
    for meals in menu.values():
        lean_meat_count = sum(1 for item in meals if item['food_item'] in lean_meats)
    while lean_meat_count < 1:
        lean_meat_food = Food.objects.filter(food__in=lean_meats).order_by('?').first()
        if lean_meat_food:
            least_meat_day = find_day_with_least_meat()
            menu[least_meat_day].append({
                'food_group': 'Meat and Alternatives',
                'food_item': lean_meat_food.food,
                'serving_size': lean_meat_food.srvg_sz,
            })
            lean_meat_count += 1

    return menu


def generate_menu_for_user_or_member(user_or_member):
    """Generate a menu for a user or family member based on serving requirements and food groups."""
    serving_requirements = get_serving_requirements(user_or_member)
    menu = {day: [] for day in ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']}

    # Apply directional statements first to meet their specific requirements
    apply_directional_statements(menu)

    # Fill in the remaining servings for each day after applying directional statements
    for requirement in serving_requirements:
        food_groups = FoodGroup.objects.filter(fgid=requirement.fgid)
        food_group = food_groups[0]
        available_foods = Food.objects.filter(fgid=food_group.fgid)
        servings = int(requirement.servings.split()[0])

        for day, meals in menu.items():
            # Calculate the remaining servings needed for each day after directional statements
            remaining_servings = servings - sum(
                1 for item in meals if item['food_group'] == food_group.foodgroup)

            for _ in range(remaining_servings):
                food_item = random.choice(available_foods)
                meals.append({
                    'food_group': food_group.foodgroup,
                    'food_item': food_item.food,
                    'serving_size': food_item.srvg_sz,
                })
            apply_whole_grain_requirement(meals)
    apply_more_veg_than_juice(menu)
    return menu


def generate_menus_for_user(user, family_member=None):
    """Generate a single weekly menu for the specified user or family member."""
    if family_member:
        # Generate a menu for the specific family member
        Menu.objects.filter(user=user, family_member=family_member).delete()

        weekly_menu = {}
        weekly_menu[f"{family_member.first_name} {family_member.last_name}"] = generate_menu_for_user_or_member(
            family_member)
        Menu.objects.create(user=user, family_member=family_member, menu_data=weekly_menu)

    else:
        # Generate a menu for the main user
        Menu.objects.filter(user=user, family_member=None).delete()

        weekly_menu = {}
        weekly_menu[user.username] = generate_menu_for_user_or_member(user)
        Menu.objects.create(user=user, menu_data=weekly_menu)

    return weekly_menu


def generate_menus_for_all_users(user):
    """Generate menus for the user and each family member."""
    # Generate menu for the main user
    generate_menus_for_user(user)

    if user.is_family_head:
        # Generate menus for each family member
        for member in user.family_members.all():
            generate_menus_for_user(user, family_member=member)
