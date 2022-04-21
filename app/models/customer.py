from django.db import models
from utils.models import CreatedUpdatedMixin
from .user import User


class Customer(CreatedUpdatedMixin):
    """
    Seperate the customer from the user. In case extra information is needed like address, phone number, bank and card details
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The phone and address can be created as a separate model and linked to the customer. In case of N number of address and phone numbers,
    phone = models.CharField(max_length=255, null=False, blank=True, default='')
    address = models.CharField(max_length=255, null=False, blank=True, default='')

    @property
    def orders(self):
        return self.customerproducthistory_set.all()
