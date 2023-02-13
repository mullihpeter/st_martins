from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact


def index(request):
    return render(request, "core_web/index.html", locals())


def contactView(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()

    return render(request, 'core_web/contact_form.html')


def successView(request):
    return HttpResponse("Success! Thank you for contacting us, we will get back to you as soon as possible.")



