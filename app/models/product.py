from django.db import models
from utils.models import CreatedUpdatedMixin


class Product(CreatedUpdatedMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity_in_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name or super().__str__()
