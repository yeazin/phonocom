# Generated by Django 4.1.1 on 2022-09-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customer_phonenumber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': 'Customer'},
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['id', 'user', 'phoneNumber'], name='accounts_cu_id_ca8aa7_idx'),
        ),
    ]
