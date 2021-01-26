from django.contrib import messages
from django.shortcuts import render, redirect

from contacts.models import Contact
from location import location


def index(request):
    data = location.sitemap()
    return render(request, 'pages/home.html', data)


def about(request):
    data = location.sitemap()
    return render(request, 'pages/about.html', data)


def contact(request):
    data = location.sitemap()
    if request.method == "POST":
        full_name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone_number"]
        subject = request.POST["msg_subject"]
        message = request.POST["message"]
        checkbox = request.POST["checkbox"]
        if checkbox == 'on':
            checkbox = True
        else:
            checkbox = False

        contact_form = Contact(
            full_name=full_name, email=email, phone=phone, subject=subject, message=message, checkbox=checkbox
        )

        contact_form.save()
        messages.success(request, "Thank you for contacting us. A representative will respond to you shortly!")
        return redirect("home")

    return render(request, 'pages/contact.html', data)


def cards(request):
    data = location.sitemap()
    return render(request, 'pages/credit-card.html', data)


def services(request):
    data = location.sitemap()
    return render(request, 'pages/services.html', data)


def documents(request):
    data = location.sitemap()
    return render(request, 'pages/documents.html', data)

#
# def index(request):
#     return render(request, 'pages/home.html')
#
#
# def index(request):
#     return render(request, 'pages/home.html')
#
#
# def index(request):
#     return render(request, 'pages/home.html')
#
#
# def index(request):
#     return render(request, 'pages/home.html')
#
#
# def index(request):
#     return render(request, 'pages/home.html')
