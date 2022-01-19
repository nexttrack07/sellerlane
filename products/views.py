from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from django.forms import modelformset_factory
# from django.contrib.auth.decorators import login_required
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
