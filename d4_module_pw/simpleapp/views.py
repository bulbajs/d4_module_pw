from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Product
from datetime import datetime
from .filters import ProductFilter
from .forms import ProductForm


class ProductList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = 'Убрал строку None'
        context['filterset'] = self.filterset
        return context


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


# def create_form(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/products/')
#     else:
#         form = ProductForm()
#
#     return render(request,'product_create.html', {'form': form})

class CreateProduct(CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_create.html'


