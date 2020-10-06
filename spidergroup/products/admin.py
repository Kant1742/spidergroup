from django.contrib import admin
from .models import Product, Category, Company


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    fiels = ('title',)


@admin.register(Category)
class Category(admin.ModelAdmin):
    model = Category


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0
    fields = ('title', )
    show_change_link = True


@admin.register(Company)
class Company(admin.ModelAdmin):
    model = Company
    fields = ('description',)
    inlines = [ProductInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'company')
    list_display_links = ('title',)
    list_filter = ('title', 'company')
    search_fields = ('title', 'id')
    save_on_top = True
