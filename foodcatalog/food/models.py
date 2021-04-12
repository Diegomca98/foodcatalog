from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100, verbose_name="Platillo")
    item_price = models.FloatField()
    item_description = models.TextField()
    item_image = models.CharField(max_length=500, default="https://www.amityinternational.com/wp-content/uploads/2019/02/product-placeholder.jpg")
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"