# Generated by Django 2.0.2 on 2019-08-01 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=268)),
                ('home', models.CharField(max_length=268)),
                ('area', models.CharField(max_length=268)),
                ('town', models.CharField(max_length=268)),
                ('state', models.CharField(max_length=268)),
                ('pin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=268)),
                ('price', models.IntegerField()),
                ('warrenty', models.IntegerField()),
                ('waterRes', models.CharField(max_length=268)),
                ('display', models.CharField(max_length=268)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]