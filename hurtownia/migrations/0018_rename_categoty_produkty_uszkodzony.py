# Generated by Django 4.0 on 2022-01-01 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0017_produkty_cena'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produkty',
            old_name='categoty',
            new_name='uszkodzony',
        ),
    ]