# Generated by Django 4.2.2 on 2023-06-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('images', models.ImageField(upload_to='pics')),
                ('details', models.TextField()),
            ],
        ),
    ]
