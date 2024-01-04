# Generated by Django 4.2 on 2023-09-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=120)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('volume', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(default='', upload_to='icecream_imgs')),
                ('user_quantity', models.PositiveIntegerField(default=1)),
                ('total_quantity', models.PositiveIntegerField(default=0)),
            ],
            options={
                'permissions': [('view_total_quantity', 'Can view total quantity')],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PopularIceCream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('volume', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(default='', upload_to='icecream_imgs')),
                ('user_quantity', models.PositiveIntegerField(default=1)),
                ('total_quantity', models.PositiveIntegerField(default=0)),
            ],
            options={
                'permissions': [('view_total_quantity', 'Can view total quantity')],
                'abstract': False,
            },
        ),
    ]