from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import *


# Create your views here.
def index(request):
    '''
    Renders the Flashcards home page template
    '''

    context = {}
    return render(request, "flashcardsApp/index.html", context)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "flashcardsApp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "flashcardsApp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "flashcardsApp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "flashcardsApp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "flashcardsApp/register.html")

def user(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404("User does not exist.")
    # return show_posts(user.username, request, posts, profile=user)
    return HttpResponseRedirect(reverse("index"))

def new_deck(request):
    return render(request, "flashcardsApp/new_deck.html")

def view_decks(request):
    '''
    Renders the Flashcards view decks page
    '''
    
    decks = Deck.objects.order_by('-title')
    context = {'decks': decks}
    return render(request, "flashcardsApp/view_decks.html", context)    

def new_card(request):
    return render(request, "flashcardsApp/new_card.html")

def view_cards(request):
    '''
    Renders the Flashcards view cards page
    '''
    
    cards = Card.objects.order_by('-question')
    context = {'cards': cards}
    return render(request, "flashcardsApp/view_cards.html", context)