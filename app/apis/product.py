from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from app.models import Product
from app.serializers import ProductSerializer, CustomerProductHistorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'place_order':
            return CustomerProductHistorySerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        request.data['user'] = str(request.user.pk)
        return super().create(request, *args, **kwargs)

    @action(
        detail=True,
        methods=['post'],
        url_path='place-order',
        permission_classes=[IsAuthenticated],
    )
    def place_order(self, request, pk=None):
        data = {**request.data, 'customer': request.user.customer.id, 'product': self.get_object().id}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            serializer.save()
            return Response(data=serializer.data)
