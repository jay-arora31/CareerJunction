# Generated by Django 4.2.4 on 2023-09-02 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadmapapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadmap',
            name='roadmap_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
