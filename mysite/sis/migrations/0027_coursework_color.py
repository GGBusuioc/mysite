# Generated by Django 2.0.1 on 2018-04-13 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0026_auto_20180412_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursework',
            name='color',
            field=models.CharField(default='#948b79', max_length=255),
        ),
    ]
