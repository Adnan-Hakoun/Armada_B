# Generated by Django 3.1.6 on 2021-02-07 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catigories',
            new_name='categories',
        ),
    ]