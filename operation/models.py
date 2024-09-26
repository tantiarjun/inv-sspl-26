from django.db import models
from master.models import Supplier, Item

class Purchase(models.Model):
    supplier_name = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.supplier_name} - {self.item_name}"


# class Purchase(models.Model):
#     invoice_no = models.CharField(max_length=20 , unique=True)
#     invoice_date = models.CharField(max_length=20)
#     supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
#     total_amount = models.PositiveIntegerField(blank=True, null=True)
#     datetime = models.DateTimeField(auto_now_add=True)
#     status = models.BooleanField(default=True)
    
#     def __str__(self):
#         return self.invoice_no
       
    
# class purchase_details(models.Model):
#     item_id = models.ForeignKey(Item ,on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(blank=True, null=True)
#     price = models.FloatField(blank=True, null=True)
#     amount = models.PositiveIntegerField(blank=True, null=True)
#     purchase_master_id = models.ForeignKey(Purchase , on_delete=models.CASCADE)
#     datetime = models.DateTimeField(auto_now_add=True)
#     status = models.BooleanField(default=1)
    
#     def __str__(self):
#         return f"{self.item_id} - {self.purchase_master_id}"
    
     
