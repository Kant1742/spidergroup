from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.views import APIView
from django_filters import rest_framework as filters

from ..models import User
from .filters import ProductFilter
from ..models import Company, Category, Product
from .serializers import (
    ProductSerializer,
    CompanySerializer,
    CategorySerializer
)

class ProductFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ('title', 'category', 'company')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related(
        'category').select_related('company')
    serializer_class = ProductSerializer
    filterset_class = ProductFilter


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_fields = '__all__'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = '__all__'
