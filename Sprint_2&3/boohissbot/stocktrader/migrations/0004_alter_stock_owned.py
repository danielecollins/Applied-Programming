# Generated by Django 3.2.8 on 2021-10-28 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocktrader', '0003_alter_stock_owned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='owned',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
