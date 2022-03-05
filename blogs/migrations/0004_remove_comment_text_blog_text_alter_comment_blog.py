# Generated by Django 4.0.1 on 2022-03-02 12:42

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_remove_blog_title_blog_name_comment_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.AddField(
            model_name='blog',
            name='text',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.blog'),
        ),
    ]
