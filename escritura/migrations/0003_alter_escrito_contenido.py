# Generated by Django 5.2.3 on 2025-06-27 19:45

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("escritura", "0002_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="escrito",
            name="contenido",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
