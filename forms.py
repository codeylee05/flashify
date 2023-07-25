from django import forms
from .models import Deck, Card


class DeckForm(forms.ModelForm):
    
    class Meta:

        model = Deck
        fields = ["deck_name", "deck_description"]

class CardForm(forms.ModelForm):

    class Meta:

        model = Card
        fields = ["prompt", "response"]