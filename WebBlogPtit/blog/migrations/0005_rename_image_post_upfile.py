# Generated by Django 3.2.9 on 2021-11-13 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='upFile',
        ),
    ]
