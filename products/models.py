import uuid
from django.db import models
from django.urls import reverse


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=250)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    cost_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    notes = models.TextField()

    def get_absolute_url(self):
        return reverse("product_detail", args=[str(self.id)])

    def __str__(self):
        return self.title


class Quote(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='quotes'
    )
    supplier = models.CharField(max_length=200)
    cost_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    misc_fees = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.supplier
    