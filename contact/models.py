from django.db import models
from django.utils import timezone


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

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
