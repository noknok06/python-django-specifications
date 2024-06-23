from django.db import models

# 商品マスタ
class ItemMst(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    item_unit = models.CharField(max_length=50)
    supplier_id = models.ForeignKey('SupplierMst', on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name

# 仕入先マスタ
class SupplierMst(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=255)

    def __str__(self):
        return self.supplier_name

# 得意先マスタ
class CustomerMst(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_address = models.TextField()

    def __str__(self):
        return self.customer_name

# 売上実績
class SalesMst(models.Model):
    sales_date = models.DateField()
    customer = models.ForeignKey(CustomerMst, on_delete=models.CASCADE)
    item_id = models.ForeignKey(ItemMst, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item_unit = models.CharField(max_length=50)

    def __str__(self):
        return f"Sales on {self.sales_date} for {self.item_id}"

# 規格変更
class StandardChangeMst(models.Model):
    update_date = models.DateField()
    item_id = models.ForeignKey(ItemMst, on_delete=models.CASCADE)
    change_details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    send_mail_flg = models.BooleanField(default=False) 
    
    def __str__(self):
        return f"Change for {self.item_id}"

class StandardChangeSendHistory(models.Model):
    send_date = models.DateField()
    customer_id = models.ForeignKey(CustomerMst, on_delete=models.CASCADE)
    item_id = models.ForeignKey(ItemMst, on_delete=models.CASCADE)
    standard_changes = models.ForeignKey(StandardChangeMst, on_delete=models.CASCADE)
    send_mail_flg = models.BooleanField(default=False) 