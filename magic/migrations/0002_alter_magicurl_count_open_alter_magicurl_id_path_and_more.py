# Generated by Django 4.1.4 on 2023-01-02 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magicurl',
            name='count_open',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='magicurl',
            name='id_path',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='magicurl',
            name='origin_url',
            field=models.URLField(max_length=2000),
        ),
    ]
