from rest_framework.generics import ListAPIView

from .models import ProductTag, ProductShort
from .serializers import TagSerializer, ProductSerializer


class TagListAPIView(ListAPIView):
    queryset = ProductTag.objects.all()
    serializer_class = TagSerializer


class ProductListAPIView(ListAPIView):
    queryset = ProductShort.objects.all()
    serializer_class = ProductSerializer
