from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=255)
    album_title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    album_logo = models.CharField(max_length=255)


    def __str__(self):
        return  self.album_title + " - " + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)