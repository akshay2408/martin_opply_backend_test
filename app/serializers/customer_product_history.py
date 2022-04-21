from rest_framework import serializers
from app.models import CustomerProductHistory


class CustomerProductHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProductHistory
        fields = '__all__'
