from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import SET_NULL, CASCADE
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Region(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Region.objects.filter(slug=self.slug).exists():
            self.slug += self.slug + '1'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Regions'
        ordering = ('-created_at',)


class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += self.slug + '1'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Categorys'
        ordering = ('-created_at',)


class Blog(BaseModel):
    user = models.ForeignKey(User, on_delete=CASCADE)
    title = models.TextField()
    image = models.ImageField(upload_to='image/')
    description = models.TextField()
    text = models.CharField(max_length=255)
    region = models.ForeignKey(Region, CASCADE)
    category = models.ForeignKey(Category, CASCADE)

    class Meta:
        db_table = 'Blogs'
        ordering = ('-created_at',)
