from django.urls import path
from .views import ProductList, ProductDetail, CreateProduct, UpdateProduct

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    # path('create/', create_form, name='product_edit')
    path('create/', CreateProduct.as_view(), name='product_edit'),
    path('<int:pk>/update/', UpdateProduct.as_view(),name='product_update'),
]

