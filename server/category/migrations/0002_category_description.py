# Generated by Django 4.0.6 on 2022-08-10 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='', verbose_name='description'),
            preserve_default=False,
        ),
    ]