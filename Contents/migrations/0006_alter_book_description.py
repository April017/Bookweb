# Generated by Django 5.0.6 on 2025-01-02 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contents', '0005_remove_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(),
        ),
    ]