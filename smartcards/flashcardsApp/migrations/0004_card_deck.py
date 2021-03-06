# Generated by Django 3.0.7 on 2020-08-04 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcardsApp', '0003_auto_20200804_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=128)),
                ('answer', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=255)),
            ],
        ),
    ]
