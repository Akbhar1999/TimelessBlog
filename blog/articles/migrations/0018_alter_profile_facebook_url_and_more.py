# Generated by Django 4.0.4 on 2022-06-09 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_profile_facebook_url_profile_instagram_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facebook_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pinterest_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]