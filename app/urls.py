from django.urls import include, path
from rest_framework.routers import SimpleRouter

from app import apis

router = SimpleRouter()
router.register('products', apis.ProductViewSet)
router.register('customers', apis.CustomerViewSet)
router.register(
    'customer-product-history',
    apis.CustomerProductHistoryViewSet,
)
router.register('users', apis.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', apis.CustomAuthToken.as_view()),
]
