# Generated by Django 5.0 on 2024-06-21 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0002_standardchangemst_update_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesmst',
            old_name='item',
            new_name='item_id',
        ),
    ]
