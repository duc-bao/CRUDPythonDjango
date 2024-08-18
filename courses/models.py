from django.db import models
from  django.contrib.auth.models import AbstractUser
from pip._vendor.rich.markup import Tag


class User(AbstractUser):
    # Dùng để thao tác với ảnh upload ảnh phải cài pillow
    avatar = models.ImageField(upload_to='lesson/%Y/%m')
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
#     Phương thức ToString
    def __str__(self):
      return self.name

class ItemBase(models.Model):
    class Meta:
        abstract = True
    subject = models.CharField(max_length=100, null=False, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='lesson/%Y/%m')
    def __str__(self):
        return self.subject

class Course(ItemBase):
    class Meta:
        unique_together = ('subject', 'category')
    description = models.TextField(null=True, blank=True)
    # Thay đổi thì tự động cập nhật
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
# Many to one
class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject', 'courses')
    content = models.TextField()
    courses = models.ForeignKey(Course,related_name="lesson", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
