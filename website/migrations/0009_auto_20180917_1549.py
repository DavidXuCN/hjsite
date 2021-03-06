# Generated by Django 2.0.7 on 2018-09-17 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_post_theme_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='website.IMG'),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
