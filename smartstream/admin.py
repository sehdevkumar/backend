from django.contrib import admin
from .models import ChannelProfile, IndividualProfile

# Register your models here.
admin.site.register(ChannelProfile)
admin.site.register(IndividualProfile)