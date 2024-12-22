from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, TableViewSet, OrderViewSet, ReservationViewSet, StaffViewSet, PaymentViewSet
from . import views
# Setting up the router
router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'tables', TableViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'payments', PaymentViewSet)

# Include the router URLs
urlpatterns = [
    path('api/', include(router.urls)),
]