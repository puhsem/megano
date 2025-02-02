# Generated by Django 5.0.6 on 2024-06-18 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(default='images/default.jpg', upload_to='images/product_images/', verbose_name='Ссылка')),
                ('alt', models.CharField(max_length=128, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('rate', models.PositiveSmallIntegerField()),
                ('date', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('value', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ProductShort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('count', models.PositiveIntegerField(default=0)),
                ('date', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=128)),
                ('freeDelivery', models.BooleanField(default=False)),
                ('reviews', models.PositiveSmallIntegerField(default=0)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.image')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.tag')),
            ],
        ),
    ]
