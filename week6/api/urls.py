from rest_framework.routers import DefaultRouter
from .views import (
    SupplierViewSet,
    CategoryViewSet,
    ProductViewSet,
    ProductSupplierViewSet
)

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-suppliers', ProductSupplierViewSet)

urlpatterns = router.urls
