# Generated by Django 3.0.7 on 2020-06-24 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20200624_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='active',
            field=models.BooleanField(auto_created=True, default=True),
        ),
    ]
