from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib import messages
from django.http import HttpResponseRedirect
from products.forms import ProductForm, PhotoForm
from products.models import Product, Photos


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'product_list'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    template_name = "products/product_create.html"
    form_class = ProductForm
    model = Product
    context_object_name = 'product'

    def post(self, request):
        form = self.get_form()
        if not form.is_valid():
            return self.form_invalid()

        images = request.FILES.getlist('images')
        product = form.save(commit=False)
        product.save()

        for image in images:
            photo = Photos.objects.create(
                product=product,
                photo=image
            )

        messages.success(request, "Product added successfully!")
        return HttpResponseRedirect("/products")

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = "/products"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if not form.is_valid():
            return self.form_invalid()

        images = request.FILES.getlist('images')
        product = self.get_object()
        form.save(commit=False)

        for image in images:
            photo = Photos.objects.create(
                product=product,
                photo=image
            )

        messages.success(request, "Product added successfully!")
        return HttpResponseRedirect("/products")


class ProductPhotoDeleteView(DeleteView):
    model = Photos

    def get_success_url(self) -> str:
        self.object = self.get_object()
        success_url = reverse('product_update', args=(self.object.product.id,))
        return success_url


class ProductDeleteView(DeleteView):
    model = Product
    success_url = 'products/'