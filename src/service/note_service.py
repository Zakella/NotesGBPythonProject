import json
import os

filename = 'data.json'


def write_data_in_file(new_dict):
    if not os.path.exists(filename):
        # If the file does not exist, create a new one with the new dictionary
        with open(filename, 'w') as file:
            json.dump([new_dict], file)
        print(f"The file '{filename}' has been created with the new dictionary.")
    else:
        # If the file exists, load the existing data and append the new dictionary
        with open(filename, 'r') as file:
            data = json.load(file)
            data.append(new_dict)
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"The new dictionary has been added to the file '{filename}'.")


def add_note(note):
    print(note)
    new_data = {'id': note.get_id(),
                'header': note.get_header(),
                'summary': note.get_summary(),
                'created': note.get_creating_date()}

    write_data_in_file(new_data)


def update_note(note_id):
    print("Update note")


def delete_note(note_id):
    print("Delete note")


def get_all_notes():
    print("get all notes")


def get_note(note_id):
    print("get note")
