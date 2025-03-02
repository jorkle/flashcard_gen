# AI (OpenAI) Anki Flashcard Generator
Generates Anki flashcards from the information on the clipboard using OpenAI API and AnkiConnector addon.

## Requirements
1. Anki (Desktop application)
2. AnkiConnector (Anki Addon)
3. pipx (to install `flashcard-gen`)
4. `xclip` installed
5. Linux OS (untested on Windows)
6. Ability to use OpenAI API

## Install
1. Install dependencies
2. Install `flashcard-gen:
  ```bash
   pipx install "git+https://github.com/jorkle/flashcard_gen"
  ```
3. Configure a keyboard shortcut in your desktop environments settings to execute the following:
  ```bash
  ~/.local/bin/flashcard-gen --api-key '<OPENAI-API-KEY' --anki-deck Bash --purpose '<PURPOSE>'
  ```
4. Replace `<PURPOSE>` with the **purpose** for the flashcards. This is used in the prompt so that the AI creates flashcards that focus on the **purpose** that you specified.
5. Replace `<OPENAI-API-KEY` with your **OpenAI API Key**.

![https://github.com/jorkle/flashcard_gen/blob/main/docs/demo.png](https://github.com/jorkle/flashcard_gen/blob/main/docs/demo.mp4)

## Usage
1. Open Anki (desktop app)
2. Find some text information that you want to create flashcards for.
3. Copy the text information to your clipboard
4. Press the hotkey that you binded the **flashcard-gen** command to in your desktop environment.
5. Wait a few seconds while it generates flashcards. It will open the "Add flashcard" dialog within a few seconds.
6. Either accept the flash card as is or tweak it to your liking. Once you add the flash card. Click the "Continue" button in the dialog popup box.
7. Repeat.. until all of the flashcards were either added or skipped.
