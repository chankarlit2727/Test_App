# Generated by Django 2.2 on 2022-07-07 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlInput', '0002_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='link_status',
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]