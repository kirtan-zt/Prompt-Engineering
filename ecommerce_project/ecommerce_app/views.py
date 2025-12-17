from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard CRUD operations for the Product model.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
