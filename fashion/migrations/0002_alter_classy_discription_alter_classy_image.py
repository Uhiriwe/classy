# Generated by Django 5.1.dev20231227050533 on 2024-01-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classy',
            name='discription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='classy',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
