from django.shortcuts import render, redirect
from django.http import HttpResponse

from cloudinary.forms import cl_init_js_callbacks

from .models import *
from .forms import VideoForm, PhotoForm


# Create your views here.
def galleryView(request):
    photo = photos.objects.all()

    ctx = {'photo': photo}

    return render(request, 'school_media/gallery.html', ctx)


def videoView(request):
    video = Videos.objects.all()

    ctx = {'video': video}

    return render(request, 'school_media/videos.html', ctx)


def addVideo(request):
    context = dict(backend_form=VideoForm())

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('videoView')
    else:
        form = VideoForm()
    return render(request, 'school_media/videos.html', context)

def addPhoto(request):
    context = dict(backend_form=PhotoForm())

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('galleryView')
    else:
        form = PhotoForm()
    return render(request, 'school_media/gallery.html', context)
