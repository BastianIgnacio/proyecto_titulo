# Generated by Django 3.2.7 on 2021-09-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='run',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]