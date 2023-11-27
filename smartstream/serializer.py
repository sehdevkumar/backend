from rest_framework import serializers
from .models import ChannelProfile, IndividualProfile

class ChannelProfileSerializer(serializers.ModelSerializer):
    channel_image = serializers.SerializerMethodField()
    class Meta:
        model = ChannelProfile
        fields = ('id', 'channel_id', 'channel_name','channel_image', 'channel_description', 'subscriber_count', 'view_count', 'video_count', 'created_at', 'updated_at')
    def get_channel_image(self, obj):
        if obj.channel_image:
            base_url = self.context['request'].build_absolute_uri('/')[:-1]  # Remove trailing slash
            return f"{base_url}{obj.channel_image.url}"
        return None

class IndividualProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualProfile
        fields = ('id', 'channel', 'bio','profile', 'social_media_links', 'website_url', 'created_at', 'updated_at')
