# Generated by Django 3.2.8 on 2021-10-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIBlog', '0003_auto_20211026_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
