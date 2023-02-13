from django.urls import path

from . import views


app_name = 'core_web'

urlpatterns = [
    path('', views.index, name='index'),
    path("contact/", views.contactView, name="contact"),
    path("success", views.successView, name="success"),
]
