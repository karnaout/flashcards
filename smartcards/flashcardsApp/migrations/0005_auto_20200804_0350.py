# Generated by Django 3.0.7 on 2020-08-04 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcardsApp', '0004_card_deck'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='flashcardsApp.Deck'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='question',
            field=models.TextField(),
        ),
    ]
