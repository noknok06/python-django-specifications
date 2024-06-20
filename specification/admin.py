from django.contrib import admin
from .models import ItemMst, SupplierMst, CustomerMst, SalesMst, StandardChangeMst

admin.site.register(ItemMst)
admin.site.register(SupplierMst)
admin.site.register(CustomerMst)
admin.site.register(SalesMst)
admin.site.register(StandardChangeMst)