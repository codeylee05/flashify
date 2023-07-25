from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import DeckForm, CardForm
from .models import Deck, Card
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    return render(request, "flashifyapp/index.html")

##DECKS
@login_required
def create_deck(request):

    if request.method == "POST":

        form = DeckForm(request.POST)
        if form.is_valid():

            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()

            return redirect("view_deck", deck_id=deck.id)
    
    else:
        
        form = DeckForm()
        return render(request, "flashifyapp/create_deck.html", {"form": form})

@login_required
def view_deck(request, deck_id):

    deck = get_object_or_404(Deck, id=deck_id, user=request.user)

    return render(request, "flashifyapp/view_deck.html", 
                  {"deck": deck, "message": "View Deck"}) 

@login_required
def view_decks(request):

    all_decks_of_user = Deck.objects.filter(user=request.user)

    return render(request, "flashifyapp/view_decks.html", {
        "decks": all_decks_of_user
    })

@login_required
def delete_deck(request, deck_id):

    deck = get_object_or_404(Deck, id=deck_id, user=request.user)

    deck.delete()

    return HttpResponse(f"Deck of id {deck_id} deleted")

##CARDS
@login_required
def create_card(request, deck_id):
    
    if request.method == "POST":

        form = CardForm(request.POST)
        if form.is_valid():

            card = form.save(commit=False)
            card.user = request.user
            card.deck_id = deck_id
            card.save()

            return redirect("view_card", card_id=card.id, deck_id=deck_id)
  
    else:

        form = CardForm()
        return render(request, "flashifyapp/create_card.html", {
            "form": form
        })

@login_required
def view_card(request, deck_id, card_id):

    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    card = get_object_or_404(Card, id=card_id, user=request.user)
    
    return render(request, "flashifyapp/view_card.html", {
        "deck": deck, "card": card, "message": "View Card"
    })

@login_required
def view_cards(request, deck_id):

    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    all_cards_of_deck = deck.cards.all()

    return render(request, "flashifyapp/view_cards.html", {
        "deck": deck, "cards": all_cards_of_deck
    })


@login_required
def delete_card(request, deck_id, card_id):

    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    card = get_object_or_404(Card, id=card_id, user=request.user)

    card.delete()

    return HttpResponse(f"Card of id {card_id} deleted")


##USERS
def user_index(request):

    if not request.user.is_authenticated:

        return HttpResponseRedirect(reverse("login"))

    return render(request, "flashifyapp/account.html")
    

def user_login(request):

    if request.method == "POST":

        user_name = request.POST["username"]
        user_pass = request.POST["password"]

        user = authenticate(username=user_name, password=user_pass)
        if user is not None:

            login(request, user)
            
            return HttpResponseRedirect(reverse("account"))
        else:

            return render(request, "flashifyapp/login.html", {
                "message": "Invalid credentials. Try again"
            })

    else:
        
        return render(request, "flashifyapp/login.html", {
            "message": "Lets get ya logged in!"
        })

@login_required
def user_logout(request):

    logout(request)

    return render(request, "flashifyapp/login.html", {
        "message": "Logged out"
    })