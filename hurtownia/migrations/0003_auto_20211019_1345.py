# Generated by Django 3.2.8 on 2021-10-19 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0002_produkty_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produkty',
            name='status',
        ),
        migrations.AddField(
            model_name='produkty',
            name='categoty',
            field=models.CharField(choices=[('Stationary', 'Stationary'), ('Electronics', 'Electronics'), ('Food', 'Food')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='produkty',
            name='kategoria',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='produkty',
            name='nazwa',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
