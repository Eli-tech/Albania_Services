# Generated by Django 3.1.2 on 2020-10-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sherbimet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='media/')),
                ('tittle', models.CharField(max_length=100)),
                ('Url', models.URLField(max_length=500)),
            ],
        ),
    ]
