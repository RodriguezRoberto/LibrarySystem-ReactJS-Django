# Generated by Django 4.0.6 on 2022-08-10 02:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_alter_invoice_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('8f3f5de7-7ca0-445b-9fd8-d46a0c6999ab')),
        ),
    ]