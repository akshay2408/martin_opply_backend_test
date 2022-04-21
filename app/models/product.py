from django.db import models
from utils.models import CreatedUpdatedMixin
from .user import User


class Product(CreatedUpdatedMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity_in_stock = models.IntegerField(default=0)
    quantity_sold = models.IntegerField(default=0)
    # Add null true in user field because the model is already migrated once.
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name or super().__str__()
