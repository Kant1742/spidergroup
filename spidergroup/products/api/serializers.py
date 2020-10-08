from rest_framework import serializers

from ..models import Category, Company, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        depth = 1


class ProductListingField(serializers.RelatedField):
    queryset = Product.objects.all()

    def to_representation(self, value):
        return value.title


class CompanySerializer(serializers.ModelSerializer):
    product_set = ProductListingField(many=True)

    class Meta:
        model = Company
        fields = '__all__'
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        depth = 2
