# Generated by Django 4.2 on 2023-05-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_comment_remove_advantagesimage_advantages_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='Comment'),
        ),
    ]
