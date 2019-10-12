# Generated by Django 2.2.6 on 2019-10-08 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('title', models.ImageField(upload_to='images/')),
            ],
        ),
    ]