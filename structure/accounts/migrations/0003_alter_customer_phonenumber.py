# Generated by Django 3.2.6 on 2022-09-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phoneNumber',
            field=models.CharField(max_length=11, null=True, unique=True, verbose_name='Phone Number'),
        ),
    ]