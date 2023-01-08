from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'role', 'is_active', 'is_superuser')
    search_fields = ('username',)
    list_filter = ('role', 'is_active', 'is_superuser')
    empty_value_display = '-пусто-'
