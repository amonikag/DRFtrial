# Generated by Django 3.2.4 on 2021-06-20 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APitry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='album',
            field=models.CharField(default='Null', max_length=500),
        ),
        migrations.AddField(
            model_name='music',
            name='name',
            field=models.CharField(default='NULL', max_length=250),
        ),
        migrations.AddField(
            model_name='music',
            name='singer',
            field=models.CharField(default='Null', max_length=250),
        ),
    ]
