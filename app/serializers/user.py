from rest_framework import serializers
from app.models import User, Customer


class UserSerializer(serializers.ModelSerializer):
    address = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'address',
            'phone',
            'is_staff',
            'is_active',
            'date_joined',
        )
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        address = validated_data.get('address')
        phone = validated_data.get('phone_number')
        Customer.objects.create(user=user, address=address, phone=phone)
        user.set_password(validated_data['password'])
        return user


class UserSerializerReadOnly(UserSerializer):
    address = serializers.CharField(source='customer.address')
    phone_number = serializers.CharField(source='customer.phone_number')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'address', 'phone_number')
        read_only_fields = ('id',)
