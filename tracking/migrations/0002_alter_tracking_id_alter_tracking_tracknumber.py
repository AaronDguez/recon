# Generated by Django 5.1.3 on 2024-11-08 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracking',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='trackNumber',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]