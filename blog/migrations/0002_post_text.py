# Generated by Django 4.1.3 on 2023-07-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='SOME STRING'),
        ),
    ]
