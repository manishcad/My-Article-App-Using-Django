# Generated by Django 4.1.5 on 2023-01-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0003_alter_article_paragraph1_alter_article_paragraph2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(blank=True, null=True, to='Article.article'),
        ),
    ]
