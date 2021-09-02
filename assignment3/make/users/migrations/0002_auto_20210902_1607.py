# Generated by Django 2.2.12 on 2021-09-02 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fav_book_genre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='categories.Category'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fav_movie_genre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='categories.Category'),
        ),
    ]
