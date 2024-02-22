# Generated by Django 3.2.11 on 2023-11-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ceshi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='name')),
                ('agen', models.IntegerField(verbose_name='agen')),
                ('size', models.IntegerField(verbose_name='size')),
            ],
            options={
                'db_table': 'ceshi',
            },
        ),
    ]
