import uuid
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=250)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    cost_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    notes = RichTextField()

    def get_absolute_url(self):
        return reverse("product_detail", args=[str(self.id)])

    def __str__(self):
        return self.title


def get_photo_filename(instance, filename):
    title = instance.product.title 
    slug = slugify(title)

    return "product_photos/%s-%s" % (slug, filename)

class Photos(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=get_photo_filename, verbose_name="Image")

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
    