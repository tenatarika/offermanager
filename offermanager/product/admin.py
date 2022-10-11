from django.contrib import admin
from django.contrib import messages
from simple_history.admin import SimpleHistoryAdmin
from simple_history.models import HistoricalRecords
from django.utils.translation import ngettext
# Register your models here.
from product.models import Product, Category, Waybill, Location, Bank


@admin.action(description='Mark selected stories as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "code", 'category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


class WaybillHistoryAdmin(SimpleHistoryAdmin):
    list_display = ('customer_name', 'count', 'finish_date', 'price', 'product', 'bank', 'location', 'document_serias',
                    'document_number',)
    history_list_display = ["status"]
    search_fields = ['name', 'user__username']

admin.site.register(Waybill, WaybillHistoryAdmin)

# @admin.register(Waybill)
# class WaybillAdmin(admin.ModelAdmin):
#     list_display = ('customer_name', 'count', 'finish_date', 'price', 'product', 'bank', 'location', 'document_serias',
#                     'document_number',)
#     actions = ['make_published']
#     def make_published(self, request, queryset):
#         self.message_user(request, ngettext('story was successfully marked as published.','stories were successfully marked as published','stories were successfully marked as published'), messages.SUCCESS)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'houseNum',)


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_number',)