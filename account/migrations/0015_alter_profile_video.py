# Generated by Django 3.2.7 on 2022-04-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20220414_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='video',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
