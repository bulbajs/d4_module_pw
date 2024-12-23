from django.urls import path
from .views import ProductList, ProductDetail, CreateProduct

urlpatterns = [
    path('', ProductList.as_view()),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    # path('create/', create_form, name='product_edit')
    path('create/', CreateProduct.as_view(), name='product_edit')
]

