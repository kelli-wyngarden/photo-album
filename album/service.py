import os

import requests

import app


def prompt_for_album():
    album = None
    try:
        album = int(input("Please enter the ID of the photo album you would like to view content for: "))
    except Exception:
        print("Invalid input. Please try again.")
    return album


def prompt_for_new_album():
    prompt = True
    while prompt is True:
        response = input("\nWould you like to view another album (Y/N)? ")
        if response.lower() in ["y", "yes"]:
            prompt = False
            os.system("cls" if os.name == "nt" else "clear")
            app.run_app()
        elif response.lower() in ["n", "no"]:
            exit()
        else:
            print("Invalid input.")


def request_photos(album_id: int):
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/photos",
            params={"albumId": album_id}
        )
        return response.json()
    except Exception:
        return []


def print_photo_album(album_id: int, photos: list):
    print(f"\nPhoto album {album_id} contains the following photos:")
    for photo in photos:
        print(f"\t{photo['id']}: {photo['title']}")
