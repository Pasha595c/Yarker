from django.db import models
from autoslug import AutoSlugField
import string
import random
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(upload_to="category_images/")
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="product_images/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=5000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
