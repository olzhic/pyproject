# Generated by Django 5.0.2 on 2024-03-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_todos_doing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='doing',
            field=models.CharField(default='nasrat', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='todos',
            name='time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
