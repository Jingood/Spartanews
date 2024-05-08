from django.contrib import admin
from .models import Jjim


@admin.register(Jjim)
class JjimAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'object_id',
                    'user', 'created_at', 'updated_at')
    readonly_fields = ('content_type', 'object_id', 'user')
