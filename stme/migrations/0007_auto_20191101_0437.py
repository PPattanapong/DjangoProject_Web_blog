# Generated by Django 2.2.6 on 2019-10-31 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stme', '0006_auto_20191101_0434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_p',
            new_name='image',
        ),
    ]
