# Generated by Django 3.1 on 2020-08-31 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=20)),
                ('postcode', models.CharField(blank=True, max_length=100)),
                ('town_or_city', models.CharField(max_length=100)),
                ('street_address1', models.CharField(max_length=100)),
                ('street_address2', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]