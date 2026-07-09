from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"

    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 13:
            raise forms.ValidationError("Age must be 13 or above.")

        return age