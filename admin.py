from django.contrib import admin
from .models import Deck, Card

# Register your models here.

class CardInline(admin.TabularInline):

    model = Card
#hence the Card model will be displayed inline the Deck Model in the admin interface

class DeckAdmin(admin.ModelAdmin):
    
    list_display = ("id", "deck_name", "deck_description")
    inlines = [CardInline] #Card Model is inline 


class CardAdmin(admin.ModelAdmin):

    list_display = ("id", "deck", "prompt", "response")


class CardInline(admin.TabularInline):

    model = Card

admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)