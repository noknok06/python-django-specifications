import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

import datetime
from django.db import models
from specification.models import ItemMst, SupplierMst, CustomerMst, SalesMst

# Djangoの設定を読み込む
# 仕入先マスタのデータを挿入
suppliers = [
    'Sony',
    'Samsung',
    'Apple',
    'LG',
    'Panasonic',
    'Toshiba',
    'Sharp',
    'Fujitsu',
    'NEC',
    'Hitachi'
]

supplier_objs = [SupplierMst(supplier_name=name) for name in suppliers]
SupplierMst.objects.bulk_create(supplier_objs)

# 商品マスタのデータを挿入
items = [
    ('PlayStation 5', 'unit', 1),
    ('Galaxy S21', 'unit', 2),
    ('iPhone 13', 'unit', 3),
    ('OLED TV', 'unit', 4),
    ('Lumix Camera', 'unit', 5),
    ('Regza TV', 'unit', 6),
    ('Aquos TV', 'unit', 7),
    ('Lifebook Laptop', 'unit', 8),
    ('VersaPro Laptop', 'unit', 9),
    ('Air Conditioner', 'unit', 10)
]

item_objs = [ItemMst(item_name=name, item_unit=unit, supplier_id_id=supplier_id) for name, unit, supplier_id in items]
ItemMst.objects.bulk_create(item_objs)

# 得意先マスタのデータを挿入
customers = [
    ('Customer A', '123 Main St, Tokyo'),
    ('Customer B', '456 Oak St, Osaka'),
    ('Customer C', '789 Pine St, Nagoya'),
    ('Customer D', '101 Maple St, Fukuoka'),
    ('Customer E', '202 Birch St, Sapporo'),
    ('Customer F', '303 Cedar St, Kyoto'),
    ('Customer G', '404 Elm St, Hiroshima'),
    ('Customer H', '505 Willow St, Sendai'),
    ('Customer I', '606 Ash St, Kanazawa'),
    ('Customer J', '707 Cherry St, Kobe')
]

customer_objs = [CustomerMst(customer_name=name, customer_address=address) for name, address in customers]
CustomerMst.objects.bulk_create(customer_objs)

# 売上実績のデータを挿入
sales = [
    (datetime.date(2023, 1, 1), 1, 1, 10, 'unit'),
    (datetime.date(2023, 1, 2), 2, 2, 20, 'unit'),
    (datetime.date(2023, 1, 3), 3, 3, 15, 'unit'),
    (datetime.date(2023, 1, 4), 4, 4, 5, 'unit'),
    (datetime.date(2023, 1, 5), 5, 5, 25, 'unit'),
    (datetime.date(2023, 1, 6), 6, 6, 8, 'unit'),
    (datetime.date(2023, 1, 7), 7, 7, 30, 'unit'),
    (datetime.date(2023, 1, 8), 8, 8, 12, 'unit'),
    (datetime.date(2023, 1, 9), 9, 9, 18, 'unit'),
    (datetime.date(2023, 1, 10), 10, 10, 22, 'unit')
]

sales_objs = [SalesMst(sales_date=date, customer_id=customer_id, item_id_id=item_id, quantity=quantity, item_unit=unit) for date, customer_id, item_id, quantity, unit in sales]
SalesMst.objects.bulk_create(sales_objs)
