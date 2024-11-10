from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MenuItemViewSet, CategoryViewSet, OrderViewSet, CartViewSet, DeliveryCrewAssignmentViewSet

# Create the router and register the viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'carts', CartViewSet)
router.register(r'delivery-assignments', DeliveryCrewAssignmentViewSet)

# Use the router URLs for the API endpoints
urlpatterns = router.urls
