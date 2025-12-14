# from django.contrib import admin
# from .models import Product

# admin.site.register(Product)

from django.contrib import admin
from .models import Product,Profile

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)

admin.site.register(Profile)