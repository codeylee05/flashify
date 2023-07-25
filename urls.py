from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("decks/create", views.create_deck, name="create_deck"),
    path("decks/viewdeck/<int:deck_id>", views.view_deck, name="view_deck"),
    path("decks/viewdecks", views.view_decks, name="viewdecks"),
    path("decks/deletedeck/<int:deck_id>", views.delete_deck, name="delete_deck"),
    path("decks/viewdeck/<int:deck_id>/cards/create", views.create_card, name="create_card"),
    path("decks/viewdeck/<int:deck_id>/cards/viewcard/<int:card_id>", views.view_card, name="view_card"),
    path("decks/viewdeck/<int:deck_id>/viewcards", views.view_cards, name="viewcards"),
    path("decks/viewdeck/<int:deck_id>/cards/deletecard/<int:card_id>", views.delete_card, name="delete_card"),
    path("user", views.user_index, name="account"),
    path("user/login", views.user_login, name="login"),
    path("user/logout", views.user_logout, name="logout"),
]