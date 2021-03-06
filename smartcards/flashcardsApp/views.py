from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import *

from .forms import DeckForm, CardForm


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
    if request.method == 'POST':
        form = DeckForm(request.POST)

        # check if form is valid
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            is_active = form.cleaned_data['is_active']

            deck = Deck(title=title, desc=desc, is_active=is_active)
            deck.save()
            return HttpResponseRedirect(reverse("view_decks"))
    else:
        form = DeckForm()

    context = {'form': form}
    return render(request, 'flashcardsApp/new_deck.html', context)

def edit_deck(request, deck_id):
    deck_obj = get_object_or_404(Deck, id=deck_id )
    if request.method == 'POST':
        form = DeckForm(request.POST, instance=deck_obj)

        # check if form is valid
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("view_decks"))    
    else:
        form = DeckForm(instance=deck_obj)

    context = {'form': form, 'edit_mode': True, 'deck_obj': deck_obj}
    return render(request, 'flashcardsApp/new_deck.html', context)

def delDeck(request, deck_id):
    deck_obj = get_object_or_404(Deck, id=deck_id)
    deck_obj.delete()
    return HttpResponseRedirect(reverse("view_decks"))  

def view_decks(request):
    '''
    Renders the Flashcards view decks page
    '''
    
    decks = Deck.objects.order_by('-title')
    context = {'decks': decks}
    return render(request, "flashcardsApp/view_decks.html", context)

def view_deck(request, deck_id):
    deck_obj = get_object_or_404(Deck, id=deck_id)
    card_list = deck_obj.card_set.all()
    card_obj = card_list.first()

    context = {''}
    return render(request, 'flashcardsApp/viewDeck.html', context)

def new_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            deck_name = form.cleaned_data['deck']
            question = form.cleaned_data['question']
            answer = form.cleaned_data['answer']
            is_active = form.cleaned_data['is_active']
            
            card = Card(deck=deck_name, question=question, answer= answer, is_active= is_active)
            card.save()
            return HttpResponseRedirect(reverse("view_cards"))
    else:
        form = CardForm()
    
    context = {'form': form}
    return render(request, "flashcardsApp/new_card.html", context)

def edit_card(request, card_id):
    card_obj = get_object_or_404(Card, id=card_id )
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card_obj)

        # check if form is valid
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("view_cards"))    
    else:
        form = CardForm(instance=card_obj)

    context = {'form': form, 'edit_mode': True, 'card_obj': card_obj}
    return render(request, 'flashcardsApp/new_card.html', context)



def del_card(request, card_id):
    card_obj = get_object_or_404(Card, id=card_id)
    card_obj.delete()
    return HttpResponseRedirect(reverse("view_cards"))  

def view_cards(request):
    '''
    Renders the Flashcards view cards page
    '''
    
    cards = Card.objects.order_by('-question')
    context = {'cards': cards}
    return render(request, "flashcardsApp/view_cards.html", context)