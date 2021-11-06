from django.contrib import admin

# Register your models here.
from product.models import Product, Category, Waybill, Location, Bank


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "code", 'category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


@admin.register(Waybill)
class WaybillAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'count', 'finish_date', 'price', 'product', 'bank', 'location', 'document_serias',
                    'document_number',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'houseNum',)


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_number',)