# Generated by Django 4.2.7 on 2023-11-29 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('image', models.CharField(max_length=500, null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('bid', models.CharField(max_length=10, null=True)),
                ('time', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
