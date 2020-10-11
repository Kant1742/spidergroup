from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics
from django_filters import rest_framework as filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import User
from .filters import ProductFilter
from ..models import Company, Category, Product
from .serializers import (
    ProductSerializer,
    CompanySerializer,
    CategorySerializer,
)
# res = Company.objects.filter(
#     location__distance_lte=(
#         ref_location,
#         D(m=distance)
#     )).order_by('distance')


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

    # def create(self, request, *args, **kwargs):

    #     serializer = self.get_serializer(
    #         data=request.data, many=isinstance(request.data, list))
    #     serializer.is_valid(raise_exception=True)
    #     # serializer.is_valid()
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, headers=headers)

class CompaniesListView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class SingleCompanyView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.filter()
    serializer_class = CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_fields = '__all__'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = '__all__'
