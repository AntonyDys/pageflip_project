# Generated by Django 2.1.5 on 2025-03-14 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pageflip', '0004_auto_20250314_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookpage',
            name='genre',
        ),
        migrations.AddField(
            model_name='bookpage',
            name='series_info',
            field=models.CharField(default='Standalone', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookpage',
            name='subgenres',
            field=models.ManyToManyField(to='pageflip.SubGenreCategory'),
        ),
        migrations.AddField(
            model_name='bookpage',
            name='year_of_publication',
            field=models.PositiveIntegerField(default=1900),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookpage',
            name='description',
            field=models.TextField(),
        ),
    ]
