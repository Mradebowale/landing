# Generated by Django 4.2.7 on 2023-11-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Message', models.TextField(max_length=10000)),
                ('email', models.EmailField(max_length=254, verbose_name=500)),
            ],
        ),
    ]
