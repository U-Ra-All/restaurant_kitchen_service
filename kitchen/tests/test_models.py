from django.test import TestCase

from kitchen.models import Cook, DishType, Dish


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
        DishType.objects.create(name="TestName")

    def test_name_label(self):
        dish_type = DishType.objects.get(id=1)
        field_label = dish_type._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        dish_type = DishType.objects.get(id=1)
        max_length = dish_type._meta.get_field("name").max_length
        self.assertEqual(max_length, 255)

    def test_dish_type_str(self):
        dish_type = DishType.objects.get(id=1)
        expected_object_name = f"{dish_type.name}"
        self.assertEqual(str(dish_type), expected_object_name)

    def test_get_absolute_url(self):
        dish_type = DishType.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(dish_type.get_absolute_url(), "/dish-types/1/")


class DishModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        dish_type = DishType.objects.create(
            name="TestName"
        )

        Cook.objects.create(
            username="test1",
            password="test12345_1",
            years_of_experience=1,
            first_name="TestFirstName1",
            last_name="TestLastName1"
        )

        Cook.objects.create(
            username="test2",
            password="test12345_2",
            years_of_experience=2,
            first_name="TestFirstName2",
            last_name="TestLastName2"
        )

        test_dish = Dish.objects.create(
            name="TestName",
            description="TestDescription",
            price=21.30,
            dish_type=dish_type,
        )

        cooks_for_dish = Cook.objects.all()
        test_dish.cooks.set(cooks_for_dish)
        test_dish.save()

    def test_name_label(self):
        dish = Dish.objects.get(id=1)
        field_label = dish._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_description_label(self):
        dish = Dish.objects.get(id=1)
        field_label = dish._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")

    def test_price_label(self):
        dish = Dish.objects.get(id=1)
        field_label = dish._meta.get_field("price").verbose_name
        self.assertEqual(field_label, "price")

    def test_dish_type_label(self):
        dish = Dish.objects.get(id=1)
        field_label = dish._meta.get_field("dish_type").verbose_name
        self.assertEqual(field_label, "dish type")

    def test_cooks_label(self):
        dish = Dish.objects.get(id=1)
        field_label = dish._meta.get_field("cooks").verbose_name
        self.assertEqual(field_label, "cooks")

    def test_name_max_length(self):
        dish = Dish.objects.get(id=1)
        max_length = dish._meta.get_field("name").max_length
        self.assertEqual(max_length, 255)

    def test_dish_str(self):
        dish = Dish.objects.get(id=1)
        expected_object_name = f"{dish.name}"
        self.assertEqual(str(dish), expected_object_name)

    def test_get_absolute_url(self):
        dish = Dish.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(dish.get_absolute_url(), "/dishes/1/")
