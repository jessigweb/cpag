# Generated by Django 2.0.3 on 2018-04-19 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_verse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verse',
            name='text',
            field=models.TextField(),
        ),
    ]
