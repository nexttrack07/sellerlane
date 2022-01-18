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
    ImageFormSet = modelformset_factory(
        Photos,
        form=PhotoForm,
        extra=6
    )

    if request.method == 'POST':
        productForm = ProductForm(request.POST)
        formset = ImageFormSet(
            request.POST,
            request.FILES,
            queryset=Photos.objects.none()
        )

        if productForm.is_valid() and formset.is_valid():
            product_form = productForm.save(commit=False)
            product_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Photos(product=product_form, image=image)
                    photo.save()
            
            messages.success(request, 'Product added successfully!')
            return HttpResponseRedirect("/products")
        else:
            print(productForm.errors, formset.errors)
    
    else:
        productForm = ProductForm()
        formset = ImageFormSet(queryset=Photos.objectsj.none())
    
    ctx = { 'productForm': productForm, 'formset': formset }
    return render(request, 'products/product_create.html', ctx)
