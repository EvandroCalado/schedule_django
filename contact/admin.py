from django.contrib import admin
from contact import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-id',)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'email', 'phone', 'created_at',)
    ordering = ('-id',)
    list_filter = ('created_at',)
    search_fields = ('id', 'first_name', 'last_name', 'email',)
    list_per_page = 10
    list_max_show_all = 100
