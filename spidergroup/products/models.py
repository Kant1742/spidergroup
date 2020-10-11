from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
# from django.contrib.gis.db import models


class User(AbstractUser):
    phone = models.IntegerField(_('phone number'), null=True)


class Company(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    description = models.TextField(_('description'), null=True, blank=True)
    is_active = models.BooleanField(_('is active'), default=False)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_('name'), max_length=200)
    # location = models.PointField(
    #     null=False, blank=False, srid=4326, verbose_name='Location')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_('name'), max_length=200)
    description = models.TextField(_('description'))
    category = models.ManyToManyField(Category)
    company = models.ForeignKey(
        _('company'), on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(_('is active'), default=False)

    @property
    def categories(self):
        return self.category_set.all()

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name
