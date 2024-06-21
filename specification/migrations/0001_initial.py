# Generated by Django 5.0 on 2024-06-21 00:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerMst',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemMst',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=255)),
                ('item_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierMst',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SalesMst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('item_unit', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specification.customermst')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specification.itemmst')),
            ],
        ),
        migrations.CreateModel(
            name='StandardChangeMst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_details', models.TextField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specification.itemmst')),
            ],
        ),
        migrations.AddField(
            model_name='itemmst',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specification.suppliermst'),
        ),
    ]
