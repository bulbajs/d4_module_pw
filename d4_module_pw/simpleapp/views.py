from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from datetime import datetime
from .filters import ProductFilter
from .forms import ProductForm
from django.urls import reverse_lazy


class ProductList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = 'Убрал строку None'
        context['filterset'] = self.filterset
        return context


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs.order_by('id')


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


class UpdateProduct(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_create.html'


class DeleteProduct(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')