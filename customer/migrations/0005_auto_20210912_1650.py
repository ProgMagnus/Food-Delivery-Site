# Generated by Django 3.2.5 on 2021-09-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_rename_is_paid_ordermodel_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='paid',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='is_paid',
            field=models.BooleanField(default=True),
        ),
    ]
