# Generated by Django 2.2.3 on 2019-09-06 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20190905_2012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['comment_time'], 'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
    ]
