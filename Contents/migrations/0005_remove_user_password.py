# Generated by Django 5.0.6 on 2025-01-02 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contents', '0004_book_author_user_is_author_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
