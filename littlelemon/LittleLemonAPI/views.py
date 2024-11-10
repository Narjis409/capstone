from rest_framework import viewsets, permissions
from .models import User, MenuItem, Category, Order, Cart, DeliveryCrewAssignment
from .serializers import UserSerializer, MenuItemSerializer, CategorySerializer, OrderSerializer, CartSerializer, DeliveryCrewAssignmentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def add_manager(self, request, pk=None):
        user = self.get_object()
        user.role = 'manager'
        user.save()
        return Response({'status': 'User is now a manager'})

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(detail=False, methods=['get'])
    def sort_by_price(self, request):
        menu_items = MenuItem.objects.all().order_by('price')
        serializer = self.get_serializer(menu_items, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def add_item(self, request, pk=None):
        cart = self.get_object()
        item = MenuItem.objects.get(id=request.data['item_id'])
        cart.items.add(item)
        return Response({'status': 'Item added to cart'})

class DeliveryCrewAssignmentViewSet(viewsets.ModelViewSet):
    queryset = DeliveryCrewAssignment.objects.all()
    serializer_class = DeliveryCrewAssignmentSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def update_order(self, request, pk=None):
        assignment = self.get_object()
        assignment.status = 'delivered'
        assignment.save()
        return Response({'status': 'Order marked as delivered'})
