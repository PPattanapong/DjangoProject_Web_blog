from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse #10
from PIL import Image #9
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):                        # สร้าง batabase ที่ชื่อว่า Post # 5
    title = models.CharField(max_length=100)  # สร้างตัวแปล title เพื่อเก็บตัวอักษร จำกัดจำนวน สูงสุด 100 ตัว
    content = models.TextField()                # เก็บข้อความ ไม่จำกัดจำนวน
    date_posted = models.DateTimeField(default=timezone.now) # เก็บวันเดือนปี ตามเวลาปัจจุบัน
    author = models.ForeignKey(User, on_delete=models.CASCADE) # เก็บข้อมูลผู้โพส
    image = models.ImageField(default='default_img.jpg', upload_to='post_img/')
    tags = TaggableManager()


# คำสั่งสร้าง db
# $ python manage.py makemigrations
# Migrations for 'stme':
#  stme\migrations\0001_initial.py
#    - Create model Post
# $ python manage.py migrate

    def __str__(self):
        return self.title

    def get_absolute_url(self): #10 กำหนดเส้นทางการกด sumit ของหน้า Post_form
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 1200 or img.width > 630:  # กำหนดรขนาดูปภาพที่อัฟโหลด
            output_size = (1200, 630)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Comment(models.Model):
    post = models.ForeignKey('stme.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

