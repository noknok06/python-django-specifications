from django.contrib import admin
from .models import ItemMst, SupplierMst, CustomerMst, SalesMst, StandardChangeMst

@admin.register(ItemMst)
class ItemMstAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'item_name', 'item_unit', 'supplier')
    search_fields = ('item_name',)

@admin.register(StandardChangeMst)
class StandardChangeMstAdmin(admin.ModelAdmin):
    list_display = ('item', 'change_details', 'supplier')
    search_fields = ('item__item_name', 'supplier__supplier_name')
    
@admin.register(CustomerMst)
class CustomerMstAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'customer_address')
    search_fields = ('customer_name',)

@admin.register(SalesMst)
class SalesMstAdmin(admin.ModelAdmin):
    list_display = ('sales_date', 'customer', 'item', 'quantity', 'item_unit')
    search_fields = ('customer__customer_name', 'item__item_name')

@admin.register(SupplierMst)
class SupplierMstAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'supplier_name')
    search_fields = ('supplier_name',)