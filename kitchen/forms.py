from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Cook, Dish


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )

    def clean(self):
        validate_years_of_experience(self.cleaned_data)


class CookUpdatingForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = ("username", "first_name", "last_name", "years_of_experience")

    def clean(self):
        validate_years_of_experience(self.cleaned_data)


def validate_years_of_experience(cleaned_data):
    years_of_experience = cleaned_data["years_of_experience"]

    if years_of_experience < 0 or years_of_experience > 80:
        raise ValidationError(
            "Number of years of experience must be " "between 0 and 80"
        )

    return years_of_experience


class CookSearchForm(forms.Form):
    username_ = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username..."}
        ),
    )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by dish name..."}
        ),
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by dish type name..."}
        ),
    )


class DishAssignOrDeleteForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = []
