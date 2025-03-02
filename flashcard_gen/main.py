#!/usr/bin/env python3

import clipboard
import sys

from argparse import ArgumentParser
from py_ankiconnect import PyAnkiconnect

from flashcard_gen.anki import Anki
from flashcard_gen.ai import AI
from flashcard_gen.gui import GUI


class FlashcardGen:

    # Constants

    def __init__(self):
        self.app_name = "AI Flashcard Generator"
        self.app_desc = "Generate flashcards from your clipboard using AI."
        self.app_usage = f"{sys.argv[0]} --api-key <api-key> --anki-deck <deck-name>"
        self.__parse_args()

    def __parse_args(self) -> None:
        arg_parser = ArgumentParser(
            prog=self.app_name, description=self.app_desc, usage=self.app_usage
        )
        arg_parser.add_argument(
            "--api-key",
            "--key",
            "-k",
            required=True,
            help="OpenAI API Key",
            dest="api_key",
        )
        arg_parser.add_argument(
            "--anki-deck",
            "--deck",
            "-d",
            required=True,
            help="Anki deck to add flashcards to",
            dest="anki_deck",
        )
        arg_parser.add_argument(
            "--purpose",
            "-p",
            required=True,
            help="State the purpose for the flashcards to be generated to help the AI generate better flashcards",
            dest="purpose",
        )
        self.args = arg_parser.parse_args()


def main():
    information = clipboard.paste()
    flashcard_gen = FlashcardGen()
    ai = AI(flashcard_gen.args.api_key)
    flashcards = ai.generate_flashcards(flashcard_gen.args.purpose, information)
    gui = GUI()
    anki = Anki(flashcard_gen.args.anki_deck)
    for flashcard in flashcards:
        if gui.prompt(flashcard.front, flashcard.back):
            anki.add_note(
                flashcard_gen.args.anki_deck,
                flashcard["front"],
                flashcard["back"],
            )
            anki.disconnect()


if __name__ == "__main__":
    main()
    sys.exit(0)
