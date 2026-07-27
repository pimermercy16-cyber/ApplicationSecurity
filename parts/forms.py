from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=50,
        required=True,
        strip=True,
    )

    def clean_q(self):
        value = self.cleaned_data["q"]

        if not value.replace(" ", "").isalnum():
            raise forms.ValidationError(
                "Only letters, numbers and spaces are allowed."
            )

        return value
    