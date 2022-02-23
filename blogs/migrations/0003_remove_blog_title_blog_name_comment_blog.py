# Generated by Django 4.0.1 on 2022-02-23 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='title',
        ),
        migrations.AddField(
            model_name='blog',
            name='name',
            field=models.CharField(default=True, max_length=60),
        ),
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blogs.blog'),
        ),
    ]
