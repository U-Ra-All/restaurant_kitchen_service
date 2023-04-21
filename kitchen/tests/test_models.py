from django.test import TestCase

from kitchen.models import Cook, DishType


class CookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Cook.objects.create(
            username="test",
            password="test12345",
            years_of_experience=5,
            first_name="TestFirstName",
            last_name="TestLastName")

    def test_username_label(self):
        cook = Cook.objects.get(id=1)
        field_label = cook._meta.get_field("username").verbose_name
        self.assertEqual(field_label, "username")

    def test_password_label(self):
        cook = Cook.objects.get(id=1)
        field_label = cook._meta.get_field("password").verbose_name
        self.assertEqual(field_label, "password")

    def test_years_of_experience_label(self):
        cook = Cook.objects.get(id=1)
        field_label = cook._meta.get_field("years_of_experience").verbose_name
        self.assertEqual(field_label, "years of experience")

    def test_first_name_label(self):
        cook = Cook.objects.get(id=1)
        field_label = cook._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "first name")

    def test_last_name_label(self):
        cook = Cook.objects.get(id=1)
        field_label = cook._meta.get_field("last_name").verbose_name
        self.assertEqual(field_label, "last name")

    def test_cook_str(self):
        cook = Cook.objects.get(id=1)
        expected_object_name = f"{cook.username} " \
                               f"({cook.first_name} {cook.last_name})"
        self.assertEqual(str(cook), expected_object_name)

    def test_get_absolute_url(self):
        cook = Cook.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(cook.get_absolute_url(), "/cooks/1/")
        
        
class DishTypeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        DishType.objects.create(name="test")

    def test_name_label(self):
        dish_type = DishType.objects.get(id=1)
        field_label = dish_type._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_dish_type_str(self):
        dish_type = DishType.objects.get(id=1)
        expected_object_name = f"{dish_type.name}"
        self.assertEqual(str(dish_type), expected_object_name)

    def test_get_absolute_url(self):
        dish_type = DishType.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(dish_type.get_absolute_url(), "/dish-types/1/")

