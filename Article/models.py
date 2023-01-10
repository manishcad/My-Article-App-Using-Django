from django.db import models
import uuid
# Create your models here.


class Base_model(models.Model):
    uid = models.UUIDField(
        default=uuid.uuid4, editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(Base_model):
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="author_image")
    paragraph1 = models.TextField(blank=True, null=True)
    paragraph2 = models.TextField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Tag(Base_model):
    name = models.CharField(max_length=100)
    articles = models.ManyToManyField('Article', null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Article(Base_model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    paragraph1 = models.TextField(blank=True, null=True, default="")
    paragraph2 = models.TextField(blank=True, null=True, default="")
    second_title = models.CharField(
        max_length=200, blank=True, null=True, default="")
    paragraph3 = models.TextField(blank=True, null=True, default="")
    paragraph4 = models.TextField(blank=True, null=True, default="")
    third_title = models.CharField(
        max_length=200, blank=True, null=True, default="")
    paragraph5 = models.TextField(blank=True, null=True, default="")
    paragraph6 = models.TextField(blank=True, null=True, default="")
    image = models.ImageField(upload_to="Article_images")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.title)
