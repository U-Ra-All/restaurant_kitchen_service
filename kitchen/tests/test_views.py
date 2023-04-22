from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Cook, DishType, Dish

DISH_TYPES_URL = reverse("kitchen:dish-type-list")
DISHES_URL = reverse("kitchen:dish-list")
COOKS_URL = reverse("kitchen:cook-list")


class PublicDishTypeListViewTest(TestCase):
    def test_login_required(self):
        response = self.client.get(DISH_TYPES_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(DISH_TYPES_URL)
        self.assertRedirects(response, "/accounts/login/?next=/dish-types/")


class PrivateDishTypeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 dish_types for pagination tests
        number_of_dish_types = 13

        for dish_type_id in range(number_of_dish_types):
            DishType.objects.create(
                name=f"TestName {dish_type_id}",
            )

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test",
            "test1234"
        )

        self.client.force_login(self.user)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/dish-types/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(DISH_TYPES_URL)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(DISH_TYPES_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")

    def test_pagination_is_5(self):
        response = self.client.get(DISH_TYPES_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["dish_type_list"]), 5)

    def test_lists_all_dish_types(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(DISH_TYPES_URL + "?page=3")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["dish_type_list"]), 3)

    def test_search_form(self):
        response = self.client.get(DISH_TYPES_URL + "?name=1")
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["is_paginated"])
        self.assertEqual(len(response.context["dish_type_list"]), 4)


class PublicDishListViewTest(TestCase):
    def test_login_required(self):
        response = self.client.get(DISHES_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(DISHES_URL)
        self.assertRedirects(response, "/accounts/login/?next=/dishes/")


class PrivateDishListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 dishes for pagination tests
        number_of_dishes = 13

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

        cooks_for_dish = Cook.objects.all()

        for dish_id in range(number_of_dishes):
            dish_type = DishType.objects.create(
                name=f"TestName {dish_id}"
            )

            test_dish = Dish.objects.create(
                name=f"TestName {dish_id}",
                description=f"TestDescription {dish_id}",
                price=21.30,
                dish_type=dish_type,
            )

            test_dish.cooks.set(cooks_for_dish)
            test_dish.save()

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test",
            "test1234"
        )

        self.client.force_login(self.user)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/dishes/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(DISHES_URL)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(DISHES_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_pagination_is_5(self):
        response = self.client.get(DISHES_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["dish_list"]), 5)

    def test_lists_all_dishs(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(DISHES_URL + "?page=3")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["dish_list"]), 3)

    def test_search_form(self):
        response = self.client.get(DISHES_URL + "?name=1")
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["is_paginated"])
        self.assertEqual(len(response.context["dish_list"]), 4)


class PublicCookListViewTest(TestCase):
    def test_login_required(self):
        response = self.client.get(COOKS_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(COOKS_URL)
        self.assertRedirects(response, "/accounts/login/?next=/cooks/")


class PrivateCookListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 8 cooks for pagination tests
        number_of_cooks = 8

        for cook_id in range(number_of_cooks):
            Cook.objects.create(
                username=f"test_{cook_id}",
                password=f"test12345_{cook_id}",
                years_of_experience=f"{cook_id}",
                first_name=f"TestFirstName{cook_id}",
                last_name=f"TestLastName{cook_id}"
            )

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test",
            "test12345"
        )

        self.client.force_login(self.user)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/cooks/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(COOKS_URL)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(COOKS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_pagination_is_5(self):
        response = self.client.get(COOKS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["cook_list"]), 5)

    def test_lists_all_cooks(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(COOKS_URL + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["cook_list"]), 4)

    def test_search_form(self):
        response = self.client.get(COOKS_URL + "?username_=1")
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["is_paginated"])
        self.assertEqual(len(response.context["cook_list"]), 1)
