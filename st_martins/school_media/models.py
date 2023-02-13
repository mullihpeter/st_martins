from django.utils import timezone
from cloudinary_storage.storage import VideoMediaCloudinaryStorage, MediaCloudinaryStorage
from cloudinary_storage.validators import validate_video
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class photos(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, storage=MediaCloudinaryStorage(),
                              validators=[])
    description = models.TextField(max_length=500, blank=True)


class Videos(models.Model):
    title = models.CharField(max_length=200, blank=True)
    video = models.FileField(upload_to='videos/', blank=True, storage=VideoMediaCloudinaryStorage(),
                              validators=[validate_video])
    description = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)