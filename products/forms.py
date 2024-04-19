from django import forms

from .models import Products

class FormProducts(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        exclude = ['user', 'like_users']