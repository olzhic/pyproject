# Generated by Django 5.0.2 on 2024-03-03 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]