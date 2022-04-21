from .customer import CustomerViewSet
from .customer_product_history import CustomerProductHistoryViewSet
from .product import ProductViewSet
from .token import CustomAuthToken
from .user import UserViewSet


__all__ = [
    CustomerViewSet,
    CustomerProductHistoryViewSet,
    ProductViewSet,
    CustomAuthToken,
    UserViewSet,
]
