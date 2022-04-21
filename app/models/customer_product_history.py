from django.db import models
from app.models.customer import Customer
from app.models.product import Product
from utils.models import CreatedUpdatedMixin


class CustomerProductHistory(CreatedUpdatedMixin):
    # Add null true in customer field because the model is already migrated once.
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
