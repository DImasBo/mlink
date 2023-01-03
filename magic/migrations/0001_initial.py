# Generated by Django 4.1.4 on 2022-12-27 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MagicURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_url', models.URLField()),
                ('id_path', models.CharField(max_length=15)),
                ('count_open', models.IntegerField()),
            ],
        ),
    ]
