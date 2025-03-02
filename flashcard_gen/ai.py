#!/usr/bin/env python3

import json

from pydantic import BaseModel
from openai import OpenAI


class Flashcard(BaseModel):
    front: str
    back: str


class FlashcardResponse(BaseModel):
    flashcards: list[Flashcard]


class AI:
    def __init__(self, api_key: str):
        self.openai_client = OpenAI(api_key=api_key)

    def generate_flashcards(self, purpose, information) -> None | list[Flashcard]:
        try:
            input = {"use_case": purpose, "information": information}

            response = self.openai_client.beta.chat.completions.parse(
                model="gpt-4o",
                messages=[
                    {
                        "role": "developer",
                        "content": "You turn information into one or more flashcards. Aa 'memory target' is the 'concept', 'idea', 'fact', or 'information' that the flashcard is intended to require you to remember. Given this definition, each flashcard must have only one 'memory target' per flashcard. Flashcards must only contain text. Markdown '**bold**' format can be used in the flashcard where logical to do so. User input will contain two items. The first item is a clearly defined 'use case' this will be identified in the input JSON by a key of 'use_case'. The second input item will be the 'information' which to generate flashcards for. this second 'information' input item will have a json key of 'information'. You must use use the 'use_case' input item to interpret the purpose that the information needs to be memorize. You will use the interpreted 'purpose' to determine what information to use for the 'memory target' for each flashcards. The json that you generate should contain a list of items containing a 'front' and 'back' JSON property.",
                    },
                    {"role": "user", "content": json.dumps(input)},
                ],
                response_format=FlashcardResponse,
            )
            data = response.choices[0].message.parsed
            if data is None:
                return
            else:
                return data.flashcards
        except Exception:
            return
