# Generated by Django 3.1.3 on 2020-11-30 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypf', '0002_auto_20201130_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='feedback',
            field=models.TextField(max_length=200),
        ),
    ]
