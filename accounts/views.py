from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ledgers.models import Ledger
from transactions.models import Wire
from django.contrib.auth.models import User


def login(request):
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
                return redirect('dashboard')
            else:
                print(user)
                print(username, password)
                print("Wrong username/password combination")
                return redirect("login")

    return render(request, "accounts/login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("home")

    return redirect("home")


@login_required(login_url='login')
def dashboard(request):
    admin_user = User.objects.filter(is_superuser=True).first()
    data = {
        "admin": admin_user
    }
    return render(request, "accounts/dashboard.html", data)


@login_required(login_url='login')
def wire_transfer(request):
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
        user_balance = user.user_ledger.balance - int(amount)
        ledger = Ledger.objects.filter(user=user).first()
        ledger.balance = user_balance
        ledger.save()
        return redirect("dashboard")

    return render(request, "accounts/transfer.html")
