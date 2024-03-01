# Generated by Django 5.0.2 on 2024-02-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_order_orderdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_order_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
