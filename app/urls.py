from django.urls import include, path
from rest_framework.routers import SimpleRouter

from app import apis

router = SimpleRouter()
router.register('products', apis.ProductViewSet, basename='products')
router.register('customers', apis.CustomerViewSet, basename='customers')
router.register(
    'customer-product-history',
    apis.CustomerProductHistoryViewSet,
    basename='customer_product_history',
)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', apis.CustomAuthToken.as_view()),
]
