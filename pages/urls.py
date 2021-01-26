from django.urls import path

from pages import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('cards/', views.cards, name="cards"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    path('documents/', views.documents, name="documents"),
]
