from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=500, verbose_name="Name ")
    product_code = models.CharField(max_length=100, unique=True, verbose_name="Product Code")
    price = models.CharField(max_length=50, verbose_name="Price")
    sale_price = models.CharField(max_length=50, null=True, blank=True, verbose_name="sale price ")

    color = models.CharField(max_length=100, null=True, blank=True, verbose_name="Color")
    memory = models.CharField(max_length=100, null=True, blank=True, verbose_name="Memory")
    manufacturer = models.CharField(max_length=200, null=True, blank=True, verbose_name="Manufacturer")

    display_size = models.CharField(max_length=100, null=True, blank=True, verbose_name="Size display")
    resolution = models.CharField(max_length=100, null=True, blank=True, verbose_name="Resolution")

    reviews_count = models.IntegerField(default=0, verbose_name="Count reviews")

    images = models.JSONField(default=list, verbose_name="Photo link")
    specs = models.JSONField(default=dict, verbose_name="characteristic")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title