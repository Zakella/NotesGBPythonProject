import json
import os
from src.view import view_notes

filename = 'data.json'


def write_data_in_file(new_data):
    if not os.path.exists(filename):
        # If the file does not exist, create a new one with the new dictionary
        with open(filename, 'w') as file:
            json.dump([new_data], file)
        print(f"The file '{filename}' has been created with the new dictionary.")
    else:
        with open(filename, 'r') as file:
            data = json.load(file)
            data.append(new_data)
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            print(f"The new record has been added to the file '{filename}'.")


def add_note(new_data):
    print(new_data)
    write_data_in_file(new_data)


def update_note(note_id, updated_values):
    print("Updating note")
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        filtered_data = list(filter(lambda record: record["id"] == note_id, data))
        if len(filtered_data) == 0:
            print(f"No note found with id {str(note_id)}")
        else:
            data = list(map(lambda record: updated_values if record["id"] == note_id else record, data))
            print(f"Updated note with id {str(note_id)}")
            with open(filename, "w") as json_file:
                json.dump(data, json_file)
                view_notes.print_result(data)


def delete_note(note_id):
    with open(filename, "r") as json_file:
        data = json.load(json_file)

        filtered_data = list(filter(lambda record: record["id"] != note_id, data))

        if len(data) == len(filtered_data):
            print(f"No note found with id {str(note_id)}")
        else:
            data = filtered_data
            print(f"Deleted note with id {str(note_id)}")

        with open(filename, "w") as json_file:
            json.dump(data, json_file)
            view_notes.print_result(data)


def get_all_notes():
    print("getting all notes")
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        view_notes.print_result(data)


def get_note(note_id):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        filtered_data = list(filter(lambda record: record["id"] == note_id, data))
        if len(filtered_data) == 0:
            print(f"No note found with id {str(note_id)}")
        else:
            view_notes.print_result(filtered_data)
