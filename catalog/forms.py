import os

from django import forms
from django.core.exceptions import ValidationError

from .models import Product

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category", "image"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "price": forms.NumberInput(attrs={"step": "0.01"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'is_published':
                self.fields[field].widget.attrs.update({'class': 'form-control'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-check-input'})

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in FORBIDDEN_WORDS:
            if word in name.lower():
                raise forms.ValidationError(f'Слово "{word}" запрещено в названии')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description:
            for word in FORBIDDEN_WORDS:
                if word in description.lower():
                    raise forms.ValidationError(f'Слово "{word}" запрещено в описании')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            return image

        # Размер файла (5 МБ = 5 * 1024 * 1024 байт)
        if image.size > 5 * 1024 * 1024:
            raise ValidationError('Размер изображения не должен превышать 5 МБ')

        # Расширение файла
        ext = os.path.splitext(image.name)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png']:
            raise ValidationError('Допустимые форматы: JPEG, PNG')

        return image
