# Generated by Django 3.2 on 2021-04-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210426_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
    ]
