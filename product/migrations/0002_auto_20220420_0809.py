# Generated by Django 3.2 on 2022-04-20 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factory',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='factory',
            name='position',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Position'),
        ),
    ]
