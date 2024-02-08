from django.db import models
from django.utils import timezone


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50,)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(default=timezone.now)
    show = models.BooleanField(default=True)
    picture = models.ImageField(
        blank=True, upload_to='media/pictures/%Y/%m/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True, )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
