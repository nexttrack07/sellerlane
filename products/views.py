from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from products.forms import ProductForm
from products.models import Product, Photos


class LoginRedirectMixin(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = '/accounts/login'

class ProductListView(LoginRedirectMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'product_list'


class ProductDetailView(LoginRedirectMixin, DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(LoginRedirectMixin, CreateView):
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
        return HttpResponseRedirect(f"/products/{product.id}")

class ProductUpdateView(LoginRedirectMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        images = request.FILES.getlist('images')
        for image in images:
            photo = Photos.objects.create(
                product=product,
                photo=image
            )
        return super().post(request, *args, **kwargs) 

        
class ProductPhotoDeleteView(LoginRedirectMixin, DeleteView):
    model = Photos

    def get_success_url(self) -> str:
        self.object = self.get_object()
        success_url = reverse('product_update', args=(self.object.product.id,))
        return success_url


class ProductDeleteView(LoginRedirectMixin, DeleteView):
    model = Product
    success_url = '/products/'