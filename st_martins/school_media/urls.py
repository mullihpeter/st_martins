from django.urls import path

from . import views


app_name = 'school_media'

urlpatterns = [
    path("", views.galleryView, name="gallery"),
    path("videos", views.videoView, name="videos"),
    path("add_video", views.addVideo, name="add_video"),
    path("add_photo", views.addPhoto, name="add_photo"),
]
