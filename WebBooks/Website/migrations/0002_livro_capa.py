# Generated by Django 4.2.6 on 2023-10-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='capa',
            field=models.ImageField(default='', upload_to='./images'),
        ),
    ]
