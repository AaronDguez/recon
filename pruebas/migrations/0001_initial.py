# Generated by Django 5.1.3 on 2024-12-10 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pruebas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'pruebas',
                'verbose_name_plural': 'pruebas',
                'db_table': 'pruebas',
            },
        ),
    ]