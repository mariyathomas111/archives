# Generated by Django 4.2 on 2023-04-06 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.CharField(max_length=355, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('citablereference', models.CharField(max_length=255)),
            ],
        ),
    ]
