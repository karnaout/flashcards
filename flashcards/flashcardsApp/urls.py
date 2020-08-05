from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path("users/<str:username>", views.user, name="user"),
    path("new_deck", views.new_deck, name="new_deck"),
    path("view_decks", views.view_decks, name="view_decks"),
    path("new_card", views.new_card, name="new_card"),
    path("view_cards", views.view_cards, name="view_cards"),
]