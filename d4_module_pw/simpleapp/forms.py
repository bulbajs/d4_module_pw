from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=25)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'quantity',
            'category',
            'price',
        ]


    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        name = cleaned_data.get('name')
        if name == description :
            # raise ValidationError({
            #     "ValidationError":"Описание совпадает с названием"
            # })
            raise ValidationError(
                'Поле совпадает с названием')
        return cleaned_data

