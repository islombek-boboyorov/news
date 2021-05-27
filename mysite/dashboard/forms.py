from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category()
        fields = "__all__"


class NewsForm(forms.ModelForm):
    class Meta:
        model = News()
        fields = "__all__"


class AuthorsForm(forms.ModelForm):
    class Meta:
        model = Authors()
        fields = "__all__"


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference()
        fields = "__all__"
