from django.urls import path

from kitchen.views import (
    index,
    CookListView,
    CookDetailView,
    DishTypeListView,
    DishTypeDetailView,
    DishListView,
    DishDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"
    ),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dish_types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list"
    ),
    path(
        "dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"
    ),
]

app_name = "kitchen"
