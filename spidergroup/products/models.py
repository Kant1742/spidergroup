from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.IntegerField(_('phone number'), null=True)


class Company(models.Model):
    # title = models.CharField(_('Title'), max_length=200) # There is not such a fild in the task list
    description = models.TextField(_('description'))
    is_active = models.BooleanField(_('is active'), default=False)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')


class Category(models.Model):
    title = models.CharField(_('title'), max_length=200)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(_('title'), max_length=200)
    description = models.TextField(_('description'))
    category = models.ManyToManyField(Category)
    company = models.ForeignKey(_('company'), on_delete=models.CASCADE)
    is_active = models.BooleanField(_('is active'), default=False)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title
