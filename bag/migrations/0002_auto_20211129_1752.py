# Generated by Django 3.2.9 on 2021-11-29 12:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
