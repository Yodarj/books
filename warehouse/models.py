'''models'''

from django.db import models
from warehouse import util

class Book(models.Model):
    """Model class for books"""

    title = models.CharField(max_length=150)
    authors = models.CharField(max_length=100)
    #we're assuming that no book is published before 0 A.D.
    publishedDate = models.IntegerField(null=True,
                                        validators=[util.not_negative])
    description = models.TextField()
    categories = models.CharField(max_length=200)

    def __str__(self):
        return self.title
