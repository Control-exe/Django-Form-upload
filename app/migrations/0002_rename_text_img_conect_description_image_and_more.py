# Generated by Django 5.0 on 2024-01-02 20:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="conect",
            old_name="text_img",
            new_name="description_image",
        ),
        migrations.RenameField(
            model_name="conect",
            old_name="img",
            new_name="image",
        ),
    ]