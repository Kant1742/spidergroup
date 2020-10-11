from django.contrib import admin
from .models import Product, Category, Company


class ProductCategoryInline(admin.TabularInline):
    model = Product.category.through
    extra = 0


@admin.register(Category)
class Category(admin.ModelAdmin):
    model = Category
    search_fields = ('name',)
    inlines = [ProductCategoryInline]


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0
    fields = ('name',)
    list_display = ('name', 'product')
    show_change_link = True


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    fiels = ('name',)
    show_change_link = True


@admin.register(Company)
class Company(admin.ModelAdmin):
    model = Company
    fields = ('description',)
    inlines = [ProductInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    list_display_links = ('name',)
    list_filter = ('name', 'company')
    search_fields = ('name', 'id')
    save_on_top = True
