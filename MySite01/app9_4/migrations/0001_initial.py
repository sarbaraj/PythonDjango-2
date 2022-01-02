# Generated by Django 3.1.3 on 2020-12-11 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', help_text='NAME', max_length=50)),
                ('contact_address', models.CharField(default='', help_text='ADDRESS', max_length=50)),
                ('mobile', models.CharField(blank=True, default='', help_text='MOBILE', max_length=50)),
                ('email', models.EmailField(blank=True, default='', help_text='EMAIL', max_length=50)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
