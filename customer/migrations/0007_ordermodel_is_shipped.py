# Generated by Django 3.2.5 on 2021-09-13 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_ordermodel_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_shipped',
            field=models.BooleanField(default=False),
        ),
    ]