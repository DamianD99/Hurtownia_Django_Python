# Generated by Django 3.1.7 on 2021-12-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0013_auto_20211208_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zamówienia',
            old_name='Klijent',
            new_name='klijent',
        ),
        migrations.RemoveField(
            model_name='zamówienia',
            name='orders',
        ),
        migrations.AddField(
            model_name='zamówienia',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
