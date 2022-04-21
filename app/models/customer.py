from django.db import models
from utils.models import CreatedUpdatedMixin
from .user import User


class Customer(CreatedUpdatedMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name or super().__str__()