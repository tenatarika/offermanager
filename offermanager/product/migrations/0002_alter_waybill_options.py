# Generated by Django 4.0 on 2021-12-20 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='waybill',
            options={'ordering': ('price', 'created_at')},
        ),
    ]
