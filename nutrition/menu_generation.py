import random
from datetime import date
from nutrition.models import FoodGroup, Food, ServingPerDay, DirectionalStatement, Menu
from accounts.models import CustomUser, FamilyMember

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

def generate_menu_for_user_or_member(user_or_member):
    """Generate a menu for a user or family member based on serving requirements and food groups."""
    serving_requirements = get_serving_requirements(user_or_member)
    menu = {day: [] for day in ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']}

    for requirement in serving_requirements:
        food_group = FoodGroup.objects.get(fgid=requirement.fgid)
        available_foods = Food.objects.filter(fgcat_id=food_group.fgcat_id)
        servings = int(requirement.servings.split()[0])  # Convert servings to int

        for _ in range(servings):
            food_item = random.choice(available_foods)
            for day in menu:
                menu[day].append({
                    'food_group': food_group.foodgroup,
                    'food_item': food_item.food,
                    'serving_size': food_item.srvg_sz,
                })

    apply_directional_statements(menu)
    return menu

def apply_directional_statements(menu):
    """Modify the menu based on directional statements for each food group."""
    directional_statements = DirectionalStatement.objects.all()

    for day, meals in menu.items():
        for statement in directional_statements:
            # Apply logic based on the directional statement's food group (fgid)
            if statement.fgid == 'vf':  # Vegetables and Fruits
                apply_vf_statements(meals)
            elif statement.fgid == 'gr':  # Grains
                apply_gr_statements(meals)
            elif statement.fgid == 'mi':  # Milk and Alternatives
                apply_mi_statements(meals)
            elif statement.fgid == 'me':  # Meat and Alternatives
                apply_me_statements(meals)

def apply_vf_statements(meals):
    """Ensure at least one dark green and one orange vegetable each day."""
    dark_green_veg = next((item for item in meals if
                           item['food_group'] == 'Vegetables and Fruit' and item['food_item'] in ['Asparagus',
                                                                                                  'Broccoli',
                                                                                                  'Spinach']), None)
    orange_veg = next((item for item in meals if
                       item['food_group'] == 'Vegetables and Fruit' and item['food_item'] in ['Carrots', 'Pumpkin',
                                                                                              'Sweet potato']), None)

    if not dark_green_veg:
        dark_green_veg_food = Food.objects.filter(fgcat_id=1).order_by('?').first()
        meals.append({
            'food_group': 'Vegetables and Fruit',
            'food_item': dark_green_veg_food.food,
            'serving_size': dark_green_veg_food.srvg_sz,
        })

    if not orange_veg:
        orange_veg_food = Food.objects.filter(fgcat_id=2).order_by('?').first()
        meals.append({
            'food_group': 'Vegetables and Fruit',
            'food_item': orange_veg_food.food,
            'serving_size': orange_veg_food.srvg_sz,
        })

def apply_gr_statements(meals):
    """Make at least half of your grain products whole grain each day."""
    total_grains = [item for item in meals if item['food_group'] == 'Grains']
    whole_grains = [item for item in total_grains if
                    item['food_item'] in ['Bread, whole grain', 'Rice, brown', 'Pasta/noodles, whole grain', 'Quinoa']]

    if len(whole_grains) < len(total_grains) / 2:
        whole_grain_food = Food.objects.filter(fgcat_id=3).order_by('?').first()
        meals.append({
            'food_group': 'Grains',
            'food_item': whole_grain_food.food,
            'serving_size': whole_grain_food.srvg_sz,
        })

def apply_mi_statements(meals):
    """Ensure that milk or milk alternatives are part of the diet each day."""
    milk_foods = [item for item in meals if item['food_group'] == 'Milk and Alternatives']

    if not milk_foods:
        milk_food = Food.objects.filter(fgid='mi').order_by('?').first()
        meals.append({
            'food_group': 'Milk and Alternatives',
            'food_item': milk_food.food,
            'serving_size': milk_food.srvg_sz,
        })

def apply_me_statements(meals):
    """Ensure that meat or meat alternatives are included."""
    meat_foods = [item for item in meals if item['food_group'] == 'Meat and Alternatives']

    if not meat_foods:
        meat_food = Food.objects.filter(fgid='me').order_by('?').first()
        meals.append({
            'food_group': 'Meat and Alternatives',
            'food_item': meat_food.food,
            'serving_size': meat_food.srvg_sz,
        })

def generate_menus_for_user(user, family_member=None):
    """Generate a single weekly menu for the specified user or family member."""
    if family_member:
        # Generate a menu for the specific family member
        Menu.objects.filter(user=user, family_member=family_member).delete()

        weekly_menu = {}
        weekly_menu[f"{family_member.first_name} {family_member.last_name}"] = generate_menu_for_user_or_member(family_member)
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
