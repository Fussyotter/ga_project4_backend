# Generated by Django 4.1.7 on 2023-03-28 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_article_user_article_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.CharField(max_length=300),
        ),
    ]
