# Generated by Django 3.2.21 on 2023-09-09 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_campaign', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='is_active',
            new_name='is_subscribed',
        ),
    ]