# Generated by Django 3.2 on 2021-10-13 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20211013_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.author', verbose_name='Автор поста'),
        ),
    ]
