# Generated by Django 4.2.1 on 2023-06-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_article_annotation_alter_article_annotation_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='instruction',
            field=models.FileField(blank=True, upload_to='reqs/', verbose_name='Инструкция оформления'),
        ),
    ]
