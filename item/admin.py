from django.contrib import admin
from .models import Category, Item
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
  list_display = ('category', 'name', 'description', 'price', 'image', 'is_sold', 'created_by', 'created_at')

admin.site.register(Category)
admin.site.register(Item, ItemAdmin)