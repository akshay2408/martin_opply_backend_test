from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from app.serializers import UserSerializer, UserSerializerReadOnly
from app.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'register' or self.action == 'create':
            return UserSerializer
        return UserSerializerReadOnly

    def get_permissions(self):
        if self.action == 'register':
            return [AllowAny()]
        return super().get_permissions()

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer = serializer.save()
        return Response(data=serializer.data)
