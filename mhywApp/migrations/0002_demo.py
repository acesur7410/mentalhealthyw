# Generated by Django 4.1.2 on 2022-10-29 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhywApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=500)),
                ('soyad', models.CharField(max_length=500)),
            ],
        ),
    ]
