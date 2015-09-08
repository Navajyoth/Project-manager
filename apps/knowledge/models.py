from django.db import models


class Quote(models.Model):
    author = models.CharField(max_length=32)
    text = models.CharField(max_length=512)

    def __unicode__(self):
        return self.author + ' - ' + self.text[:16]


class Article(models.Model):
    url = models.URLField(max_length=256)
    title = models.CharField(max_length=256)

    def __unicode__(self):
        return self.title
