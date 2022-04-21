from rest_framework.viewsets import ModelViewSet
from app.models import CustomerProductHistory
from app.serializers import CustomerProductHistorySerializer


class CustomerProductHistoryViewSet(ModelViewSet):
    queryset = CustomerProductHistory.objects.all()
    serializer_class = CustomerProductHistorySerializer
