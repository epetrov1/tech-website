# Generated by Django 3.2 on 2021-09-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_blogpost_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
