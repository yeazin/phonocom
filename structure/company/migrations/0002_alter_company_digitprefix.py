# Generated by Django 4.1.1 on 2022-09-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='digitprefix',
            field=models.CharField(max_length=3, null=True, verbose_name='Digit Prefix'),
        ),
    ]
