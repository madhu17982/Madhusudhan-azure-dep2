# Generated by Django 3.2.8 on 2022-10-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racks', '0002_rename_rackazure_rack_azure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack_azure',
            name='explanation',
            field=models.TextField(null=True),
        ),
    ]
