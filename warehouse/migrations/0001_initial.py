# Generated by Django 2.1 on 2019-05-18 19:27

from django.db import migrations, models
import warehouse.util


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('authors', models.CharField(max_length=100)),
                ('publishedDate', models.IntegerField(null=True, validators=[warehouse.util.not_negative])),
                ('description', models.TextField()),
                ('categories', models.CharField(max_length=200)),
            ],
        ),
    ]
