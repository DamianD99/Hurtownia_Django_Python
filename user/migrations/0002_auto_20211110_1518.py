# Generated by Django 3.1.7 on 2021-11-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='adress', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='phone', max_length=50),
        ),
    ]
