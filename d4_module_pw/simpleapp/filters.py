from django_filters import FilterSet, CharFilter, NumberFilter
from .models import Product


class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains', label='Название')
    quantity = NumberFilter(lookup_expr='gt', label='Кол-во больше')
    price_gt = NumberFilter(field_name='price', lookup_expr='gt', label='Цена выше')
    price_lt = NumberFilter(field_name='price', lookup_expr='lt', label='Цена ниже')

    class Meta:
        model = Product
        fields = ['name', 'quantity']