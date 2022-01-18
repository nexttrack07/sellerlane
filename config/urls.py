from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    # User management
    path('accounts/', include('allauth.urls')),
    # Local
    path('', include('pages.urls')),
    path('products/', include('products.urls')),
]
