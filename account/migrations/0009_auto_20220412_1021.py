# Generated by Django 3.2.7 on 2022-04-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='caption',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='video',
            field=models.FileField(null=True, upload_to='account/%y'),
        ),
    ]
