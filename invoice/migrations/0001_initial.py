# Generated by Django 3.2.7 on 2021-10-22 09:29

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('customer_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('billing_address', models.CharField(blank=True, max_length=250, null=True)),
                ('floor', models.IntegerField(null=True)),
                ('date', models.DateField()),
                ('due_date', models.DateField()),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('status', models.BooleanField(default=False)),
                ('market', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.market')),
            ],
            options={
                'ordering': ('due_date',),
            },
        ),
    ]
