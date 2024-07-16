# Generated by Django 5.0.7 on 2024-07-15 05:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
                ('author', models.CharField(max_length=123)),
                ('file', models.FileField(upload_to='media/musics')),
                ('music_text', models.TextField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.genre')),
            ],
        ),
    ]