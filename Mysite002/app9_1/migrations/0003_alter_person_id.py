# Generated by Django 4.0 on 2022-01-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app9_1', '0002_auto_20201211_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]