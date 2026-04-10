from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SupplierViewSet,
    CategoryViewSet,
    ProductViewSet,
    ProductSupplierViewSet,
    DashboardAPIView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register("suppliers", SupplierViewSet)
router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)
router.register("product-suppliers", ProductSupplierViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("dashboard/", DashboardAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
