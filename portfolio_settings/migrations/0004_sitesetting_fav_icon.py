# Generated by Django 3.2 on 2021-04-30 16:15

from django.db import migrations, models
import portfolio_settings.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_settings', '0003_auto_20210426_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='fav_icon',
            field=models.ImageField(null=True, upload_to=portfolio_settings.models.upload_image_path),
        ),
    ]
