from rest_framework import serializers
from app.models import CustomerProductHistory


class CustomerProductHistorySerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, required=True)

    class Meta:
        model = CustomerProductHistory
        fields = ['id', 'customer', 'product', 'amount', 'quantity']
        read_only_fields = ['amount']  # amount is calculated in the create method

    def create(self, validated_data):
        product = validated_data['product']
        quantity = validated_data['quantity']
        amount = product.price * quantity
        validated_data['amount'] = amount

        product.quantity_in_stock -= quantity
        product.quantity_sold += quantity
        product.save()

        return super().create(validated_data=validated_data)


class CustomerProductHistoryReadOnlySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerProductHistory
        fields = '__all__'
