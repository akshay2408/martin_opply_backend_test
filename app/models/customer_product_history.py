from django.db import models
from utils.models import CreatedUpdatedMixin
from .user import User


class CustomerProductHistory(CreatedUpdatedMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.customer_name or super().__str__()
