from cloudinary.forms import CloudinaryFileField
from django.forms import ModelForm
from .models import *


class VideoForm(ModelForm):
    class Meta:
        model = Videos
        fields = "__all__"

        video = CloudinaryFileField(
            options={
                'tags': "directly_uploaded",
                'crop': 'limit', 'width': 1000, 'height': 1000,
                'eager': [{'crop': 'fill', 'width': 150, 'height': 100}]
            })


class PhotoForm(ModelForm):
    class Meta:
        model = photos
        fields = "__all__"

        image = CloudinaryFileField(
            options={
                'tags': "directly_uploaded",
                'crop': 'limit', 'width': 1000, 'height': 1000,
                'eager': [{'crop': 'fill', 'width': 150, 'height': 100}]
            })
