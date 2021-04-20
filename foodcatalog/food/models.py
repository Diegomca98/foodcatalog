from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100, verbose_name="Name")
    item_price = models.FloatField()
    item_description = models.CharField(max_length=500, verbose_name="Description")
    item_image = models.CharField(max_length=500, default="https://www.amityinternational.com/wp-content/uploads/2019/02/product-placeholder.jpg")
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def get_absolute_url(self):
        return reverse("details", kwargs={"pk": self.pk})
    