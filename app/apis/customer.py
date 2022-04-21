from rest_framework.viewsets import ModelViewSet
from app.models import Customer
from app.serializers import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
