from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from app.models import Customer
from app.serializers import CustomerSerializer, CustomerProductHistoryReadOnlySerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_serializer_class(self):
        if self.action == 'orders':
            return CustomerProductHistoryReadOnlySerializer
        return super().get_serializer_class()

    @action(detail=True, methods=['get'])
    def orders(self, request, pk=None):
        customer = self.get_object()
        orders = customer.orders.all()
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)
