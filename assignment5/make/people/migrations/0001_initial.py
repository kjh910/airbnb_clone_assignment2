# Generated by Django 3.1 on 2020-09-03 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
                ('photo', models.ImageField(upload_to='')),
                ('kind', models.CharField(choices=[('actor', 'Actor'), ('director', 'Director'), ('writer', 'Writer')], max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
