from rest_framework.viewsets import ModelViewSet
from app.serializers import UserSerializer
from app.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
