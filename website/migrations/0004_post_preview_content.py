# Generated by Django 2.0.7 on 2018-08-08 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20180808_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview_content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
