# Generated by Django 4.1.2 on 2022-10-30 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhywApp', '0004_alter_duyuru_baslik_alter_duyuru_baslikar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='duyuru',
            name='baslangic',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duyuru',
            name='bitis',
            field=models.DateField(blank=True, null=True),
        ),
    ]