# Generated by Django 3.2.6 on 2021-08-31 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='fav_book_genre',
            field=models.CharField(choices=[('action', 'Action'), ('comedy', 'Comedy'), ('thriller', 'Thriller'), ('history', 'History')], default='history', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='fav_movie_genre',
            field=models.CharField(choices=[('action', 'Action'), ('comedy', 'Comedy'), ('thriller', 'Thriller'), ('history', 'History')], default='history', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('english', 'English'), ('korean', 'Korean')], default='english', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='preference',
            field=models.CharField(choices=[('books', 'Books'), ('movies', 'Movies')], default='movies', max_length=20),
        ),
    ]
