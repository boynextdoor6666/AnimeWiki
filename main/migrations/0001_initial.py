    # Generated by Django 5.0 on 2023-12-17 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='name')),
                ('age', models.CharField(default='', max_length=2, verbose_name='age')),
                ('story', models.TextField(verbose_name='story')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/')),
            ],
        ),
    ]