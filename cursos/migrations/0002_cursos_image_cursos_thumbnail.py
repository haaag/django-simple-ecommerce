# Generated by Django 4.0.6 on 2022-07-05 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='cursos',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]