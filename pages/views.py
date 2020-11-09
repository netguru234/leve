from django.shortcuts import render, redirect

from contacts.models import Contact


def index(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
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
        return redirect("home")

    return render(request, 'pages/contact.html')


def cards(request):
    return render(request, 'pages/credit-card.html')


def services(request):
    return render(request, 'pages/services.html')


def team(request):
    return render(request, 'pages/team.html')

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
