# Generated by Django 3.0.7 on 2020-06-24 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authors',
            new_name='author',
        ),
    ]