from django.urls import path
from .views import ProductList, ProductDetail, create_form


urlpatterns = [
    path('', ProductList.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
    path('create/', create_form, name='product_edit')
]

