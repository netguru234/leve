from django.urls import path

from accounts import views

urlpatterns = [
    path("sign_in", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("transfer", views.wire_transfer, name='transfer'),
]
