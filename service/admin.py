from django.contrib import admin
from .models import Item
from django.db.models import F


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_display_links = ('id',)
    list_editable = ('name', 'description', 'price')
    list_per_page = 3
    ordering = ['name']
    search_fields = ['name__startswith']

    actions = ['increase_price_action']

    @admin.action(description="Increase price by 10000")
    def increase_price_action(self, request, queryset):
        count = queryset.update(price=F('price') + 10000)
        self.message_user(request, f"Change {count} items.")
