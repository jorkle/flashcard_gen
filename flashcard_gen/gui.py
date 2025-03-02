import FreeSimpleGUI as sg
import time


class GUI:

    def __init__(self):
        pass

    def prompt(self) -> None:
        sg.theme("DarkGrey15")
        #        column_layout1 = [
        #            [
        #                sg.Text("Front:"),
        #                sg.Text(flashcard_front, key="-FRONT-", size=(30, 15)),
        #            ]
        #        ]
        #        column_layout2 = [
        #            [
        #                sg.Text("Back:"),
        #                sg.Text(
        #                    flashcard_back,
        #                    key="-BACK-",
        #                    size=(30, 15),
        #                ),
        #            ]
        #        ]
        #
        #        column_layout3 = [[sg.Button("Skip"), sg.Button("Create")]]
        #
        #        layout = [
        #            [
        #                sg.Column(column_layout1, element_justification="top"),
        #            ],
        #            [
        #                sg.Column(column_layout2, element_justification="center"),
        #            ],
        #            [
        #                sg.Column(column_layout3, element_justification="center"),
        #            ],
        #        ]
        #
        layout = [
            [
                sg.Column(
                    [
                        [
                            sg.Text("Click 'Continue' when done with current card"),
                            sg.Button("Continue"),
                        ]
                    ]
                )
            ]
        ]
        window = sg.Window("Continue..", layout)
        event, values = window.Read()

        if event == "CONTINUE":
            return
