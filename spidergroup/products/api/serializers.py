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
        return value.name

    def to_internal_value(self, data):
        # print(data)
        return data


class CompanySerializer(serializers.ModelSerializer):
    products = ProductListingField(
        many=True, required=False, source='product_set')

    class Meta:
        model = Company
        fields = '__all__'
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

    def update(self, instance, validated_data):
        products = validated_data.pop('product_set')
        instance.products = products
        for prod in products:
            Product.objects.create(name=prod, company_id=instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    company = CompanySerializer(required=False)
    category = CategorySerializer(required=False)

    class Meta:
        model = Product
        fields = '__all__'
        depth = 2

    def create(self, validated_data):
        categories = validated_data.pop('category')

        # TODO need to get company id from request
        company = Company.objects.get_or_create(id=3)
        try:
            for i in company:
                print(i)
                product = Product.objects.update_or_create(
                    company=i, category__name=categories['name'], **validated_data)
        except:
            print('Forloop exception')
        try:
            product.save()
        except AttributeError:
            print('Save exception')
        return product

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description',
    #                                               instance.description)

    #     instance.save()
    #     return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
