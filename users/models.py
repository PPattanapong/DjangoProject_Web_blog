from django.db import models
from django.contrib.auth.models import User
from PIL import Image #9
# Create your models here.

class Profile(models.Model):  #8    #pip install Pillow
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # https://pypi.org/project/Pillow/
    # > pip install Pillow
    # > python manage.py makemigrations
    #    Migrations for 'users':
    #    users\migrations\0001_initial.py
    #    - Create model Profile
    # > python manage.py migrate
    #    Apply all migrations: admin, auth, contenttypes, sessions, stme, users
    #    Running migrations:
    #    Applying users.0001_initial...OK

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300: # กำหนดรขนาดูปภาพที่อัฟโหลด
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



