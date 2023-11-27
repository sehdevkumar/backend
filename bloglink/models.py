from django.db import models


class Blog(models.Model):
    title = models.TextField(max_length=200,null=True)
    user_id = models.IntegerField()
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)