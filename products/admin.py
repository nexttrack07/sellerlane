from django.contrib import admin
from .models import Product, Quote

class QuoteInline(admin.TabularInline):
    model = Quote

class ProductAdmin(admin.ModelAdmin):
    inlines = [QuoteInline,]
    list_display = ("title", "sale_price", "cost_per_unit")

admin.site.register(Product, ProductAdmin)
