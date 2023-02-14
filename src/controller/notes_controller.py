import os
from datetime import date

from src.model.Note import Note
from src.service import note_service


def start_application():
    note_id = 1

    filename = "data.json"

    if os.path.exists(filename):
        os.remove(filename)

    while True:
        command_input = input("Please enter command: ")
        if command_input == "stop":
            print("Application stopped")
            break
        elif command_input == "add":

            header = input("Please enter header: ")
            summary = input("Please enter summary: ")
            note = Note(note_id, header, summary, str(date.today()))
            note_service.add_note(note)
            note_id = note_id + 1

        elif command_input == "delete":

            note_id = int(input("Please enter note id: "))
            note_service.delete_note(note_id)

        elif command_input == "update":

            note_id = int(input("Please enter note id: "))
            header = input("Please enter header: ")
            summary = input("Please enter summary: ")
            note_service.delete_note(note_id)
            note = Note(note_id, header, summary, str(date.today()))

        elif command_input == "get all":

            note_service.get_all_notes()

        elif command_input == "get by id":

            note_id = int(input("Please enter note id: "))
            note_service.get_note(note_id)

        else:
            print("Unknown command: ", command_input)
