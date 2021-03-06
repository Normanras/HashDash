# Generated by Django 4.0.4 on 2022-05-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('social_media', models.CharField(choices=[('HC', 'Home Assistant Community'), ('RD', 'Reddit'), ('TW', 'Twitter'), ('FB', 'Facebook'), ('TT', 'Tik-Tok')], default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dashboard', models.ImageField(upload_to='')),
                ('dash_name', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='dashCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dash_name', models.CharField(max_length=50)),
                ('yaml', models.TextField()),
            ],
        ),
    ]
