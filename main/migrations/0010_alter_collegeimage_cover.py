# Generated by Django 4.0.6 on 2022-10-01 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_collegeimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeimage',
            name='cover',
            field=models.ImageField(default='default.jpg', upload_to='col_images'),
        ),
    ]
