from django.db import models


class ChannelProfile(models.Model):
    channel_id = models.CharField(max_length=255, unique=True)
    channel_name = models.CharField(max_length=255)
    channel_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    channel_description = models.TextField()
    subscriber_count = models.IntegerField()
    view_count = models.IntegerField()
    video_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.channel_name


class IndividualProfile(models.Model):
    channel = models.ForeignKey(ChannelProfile, on_delete=models.CASCADE)
    bio = models.TextField()
    profile = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    social_media_links = models.CharField(max_length=255) 
    website_url = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
