# Generated by Django 4.0.6 on 2022-10-01 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_collegeimage_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locality', models.CharField(max_length=100)),
                ('bus_no', models.IntegerField()),
                ('fees', models.IntegerField()),
            ],
        ),
    ]
