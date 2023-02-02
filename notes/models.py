from django.db import models


class Notes(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
