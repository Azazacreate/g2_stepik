# Generated by Django 5.1.3 on 2025-03-21 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_movie", "0010_rename_director_movie_director2"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie",
            old_name="director2",
            new_name="director",
        ),
    ]
