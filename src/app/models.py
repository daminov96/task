from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name


class Musics(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')

    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    musics = models.ManyToManyField(Musics, related_name="category")

    def __str__(self):
        return self.title