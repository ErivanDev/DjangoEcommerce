# Generated by Django 4.1.2 on 2022-10-17 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='variatoin_value',
            new_name='variation_value',
        ),
    ]
