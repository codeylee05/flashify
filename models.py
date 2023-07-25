from django.db import models
from django.contrib.auth.models import User


class Deck(models.Model):

    deck_name = models.CharField(max_length=100)
    deck_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="deck_owner", default=1)

    def __str__(self):
        return f"Deck: {self.deck_name}, Description: {self.deck_description}"
    

class Card(models.Model):

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="cards")
    prompt = models.CharField(max_length=64)
    response = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="card_owner", default=1)


    def __str__(self):

        return f"Card: {self.prompt}, Response: {self.response}, Deck: {self.deck.deck_name}"
