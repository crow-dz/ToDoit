# Generated by Django 3.1 on 2020-08-28 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='LastName',
            field=models.CharField(default='name', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='firstName',
            field=models.CharField(default='name', max_length=30),
        ),
    ]
