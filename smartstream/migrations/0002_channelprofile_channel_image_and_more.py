# Generated by Django 4.2.2 on 2023-11-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartstream', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channelprofile',
            name='channel_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
        migrations.AddField(
            model_name='individualprofile',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]