# Generated by Django 3.2.7 on 2021-10-22 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_alter_invoice_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ('due_date',)},
        ),
    ]
