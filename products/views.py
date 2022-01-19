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
    context_object_name = 'product'


def create_product(request):

    if request.method == 'POST':
        productForm = ProductForm(request.POST)
        images = request.FILES.getlist('images')
        

        if productForm.is_valid():
            product_form = productForm.save(commit=False)
            product_form.save()

            for image in images:
                photo = Photos.objects.create(
                    product=product_form,
                    photo=image
                )

            
            messages.success(request, 'Product added successfully!')
            return HttpResponseRedirect("/products")
        else:
            print(productForm.errors)
    
    else:
        productForm = ProductForm()
    
    ctx = { 'productForm': productForm }
    return render(request, 'products/product_create.html', ctx)
