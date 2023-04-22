from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.urls import reverse

from kitchen.forms import CookCreationForm, CookUpdatingForm
from kitchen.models import Cook, DishType, Dish


class CookCreationFormTest(TestCase):
    def test_cook_create_form_years_of_experience_label(self):
        form = CookCreationForm()
        self.assertTrue(
            (form.fields["years_of_experience"].label is None
             or form.fields["years_of_experience"].label == "Years of experience")
        )

    def test_cook_create_form_years_of_experience_is_negative(self):
        data = {
            "username": "test_user",
            "years_of_experience": -1,
            "password1": "test12345test",
            "password2": "test12345test",
            "first_name": "Test",
            "last_name": "Test"
        }

        form = CookCreationForm(data)
        self.assertFalse(form.is_valid())

    def test_cook_create_form_years_of_experience_is_more_than_80(self):
        data = {
            "username": "test_user",
            "years_of_experience": 81,
            "password1": "test12345test",
            "password2": "test12345test",
            "first_name": "Test",
            "last_name": "Test"
        }

        form = CookCreationForm(data)
        self.assertFalse(form.is_valid())

    def test_cook_create_form_years_of_experience_is_valid(self):
        data = {
            "username": "test_user",
            "years_of_experience": 8,
            "password1": "test12345test",
            "password2": "test12345test",
            "first_name": "Test",
            "last_name": "Test"
        }

        form = CookCreationForm(data=data)
        self.assertTrue(form.is_valid())


class CookUpdatingFormTest(TestCase):
    def test_cook_update_form_years_of_experience_label(self):
        form = CookUpdatingForm()
        self.assertTrue(
            (form.fields["years_of_experience"].label is None
             or form.fields["years_of_experience"].label == "Years of experience")
        )

    def test_cook_update_form_years_of_experience_is_negative(self):
        data = {
            "username": "test_user",
            "years_of_experience": -1,
            "first_name": "Test",
            "last_name": "Test"
        }

        form = CookUpdatingForm(data)
        self.assertFalse(form.is_valid())

    def test_cook_update_form_years_of_experience_is_more_than_80(self):
        data = {
            "username": "test_user",
            "years_of_experience": 81,
            "first_name": "Test",
            "last_name": "Test"
        }

        form = CookUpdatingForm(data)
        self.assertFalse(form.is_valid())

    def test_cook_update_form_years_of_experience_is_valid(self):
        data = {
            "username": "test_user",
            "years_of_experience": 8,
            "first_name": "Test",
            "last_name": "Test"
        }

        form = CookUpdatingForm(data=data)
        self.assertTrue(form.is_valid())


class UpdateFormsHaveInitialValuesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_user(
            username="test_1",
            password="test12345_1",
            years_of_experience=1,
            first_name="TestFirstName_1",
            last_name="TestLastName_1"
        )

        get_user_model().objects.create_user(
            username="test_2",
            password="test12345_2",
            years_of_experience=2,
            first_name="TestFirstName_2",
            last_name="TestLastName_2"
        )

        dish_type = DishType.objects.create(
            name="TestName",
        )

        cooks_for_dish = Cook.objects.all()
        test_dish = Dish.objects.create(
            name="TestName",
            description="TestDescription",
            price=11,
            dish_type=dish_type)

        test_dish.cooks.set(cooks_for_dish)
        test_dish.save()

    def setUp(self):
        user = get_object_or_404(Cook, username="test_1")
        self.client.force_login(user)

    def test_cook_update_form_has_initial_value(self):
        response = self.client.get(reverse(
            "kitchen:cook-update",
            kwargs={"pk": 1}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["form"].initial["username"],
            "test_1"
        )
        self.assertEqual(
            response.context["form"].initial["first_name"],
            "TestFirstName_1"
        )
        self.assertEqual(
            response.context["form"].initial["last_name"],
            "TestLastName_1"
        )
        self.assertEqual(
            response.context["form"].initial["years_of_experience"],
            1
        )

    def test_dish_type_update_form_has_initial_value(self):
        response = self.client.get(reverse(
            "kitchen:dish-type-update",
            kwargs={"pk": 1}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["form"].initial["name"],
            "TestName"
        )

    def test_dish_update_form_has_initial_value(self):
        cooks_for_dish = Cook.objects.all()
        response = self.client.get(reverse(
            "kitchen:dish-update",
            kwargs={"pk": 1}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["form"].initial["name"],
            "TestName"
        )
        self.assertEqual(
            response.context["form"].initial["description"],
            "TestDescription"
        )
        self.assertEqual(
            response.context["form"].initial["price"],
            11
        )
        self.assertEqual(
            response.context["form"].initial["dish_type"],
            1
        )
        self.assertEqual(
            response.context["form"].initial["cooks"],
            list(cooks_for_dish)
        )
