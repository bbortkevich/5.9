# Generated by Django 4.1.2 on 2022-10-14 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_comment_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=10000),
        ),
    ]
