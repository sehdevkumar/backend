# Generated by Django 4.2.6 on 2023-11-17 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloglink', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
