# Generated by Django 2.2.6 on 2019-10-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stme', '0003_post_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post_img',
        ),
        migrations.AddField(
            model_name='post',
            name='image_p',
            field=models.ImageField(default='default_img.jpg', upload_to='post_img'),
        ),
    ]
