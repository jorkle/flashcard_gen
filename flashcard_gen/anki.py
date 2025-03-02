#!/usr/bin/env python3

import sys

from py_ankiconnect import PyAnkiconnect


class Anki:
    def __init__(self, deck_name: str):
        self.anki = PyAnkiconnect()
        self.deck_name = deck_name
        self.__deck_exists(deck_name)

    def __deck_exists(self, deck_name):
        decks = self.anki("deckNames")
        if deck_name not in decks:
            print("deck does not exist")
            sys.exit(1)

    def add_card(self, front: str, back: str) -> None:
        self.anki(
            "guiAddCards",
            note={
                "deckName": self.deck_name,
                "modelName": "Basic",
                "fields": {"Front": front, "Back": back},
                "options": {"allowDuplicate": False},
            },
        )
