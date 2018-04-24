# Generated by Django 2.0.3 on 2018-04-19 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20180411_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verse', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=1000)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
