from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.conf import settings
# from django.http import HttpResponse
from twilio.rest import Client

from ledgers.models import Ledger
from location import location
from transactions.models import Wire
from django.contrib.auth.models import User


def login(request):
    data = location.sitemap()
    # check_user = User.objects.check(username=request.user.username)

    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                print(user)
                print(username, password)
                auth.login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('dashboard')
            else:
                messages.error(request, "Wrong username/password combination")
                # print(user)
                # print(username, password)
                # print("Wrong username/password combination")
                return redirect("login")

    return render(request, "accounts/login.html", data)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are successfully logged out!")
        return redirect("home")

    return redirect("home")


@login_required(login_url='login')
def dashboard(request):
    admin_user = User.objects.filter(is_superuser=True).first()
    data = {
        "admin": admin_user,
    }
    return render(request, "accounts/dashboard.html", data)


@login_required(login_url='login')
def wire_transfer(request):
    data = location.sitemap()
    if request.method == "POST":
        user = request.user
        amount = request.POST["amount"]
        bank_name = request.POST["bank_name"]
        acct_num = request.POST["acct_num"]
        swift_code = request.POST["swift_code"]
        bank_address = request.POST["bank_address"]
        bank_phone = request.POST["bank_phone"]
        country = request.POST["country"]
        state = request.POST["state"]
        zip_code = request.POST["zip_code"]
        recipient = request.POST["recipient"]

        funds_transfer = Wire(
            acct_owner=user, amount=amount, bank_name=bank_name, acct_num=acct_num, swift_code=swift_code,
            bank_address=bank_address, bank_phone=bank_phone, country=country, state=state, zip_code=zip_code,
            recipient=recipient
        )
        funds_transfer.save()
        # print(user.user_ledger.phone, settings.TWILIO_NUMBER)
        # print(send_sms.sid)
        user_balance = user.user_ledger.balance - int(amount)
        ledger = Ledger.objects.filter(user=user).first()
        ledger.balance = user_balance
        ledger.save()
        message_to_broadcast = f"TRANSFER ALERT!!! Your transfer of USD{amount} was successfully " \
                               f"completed!\nAvailable " \
                               f"Balance: USD{user.user_ledger.balance}"
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        send_sms = client.messages.create(to=user.user_ledger.phone,
                                          from_=settings.TWILIO_NUMBER,
                                          body=message_to_broadcast)
        messages.success(request, "Transfer completed successfully!")
        return redirect("dashboard")

    return render(request, "accounts/transfer.html", data)
