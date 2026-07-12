from django import forms
from django.core.validators import MinLengthValidator

class AddRestaurantForm(forms.Form):

    restaurant_name = forms.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)]
    )

    cuisine_type = forms.CharField(
        max_length=100
    )

    contact_email = forms.EmailField()