import requests


def prompt_for_album():
    album = None
    try:
        album = int(input("Please enter the ID of the photo album you would like to view content for: "))
    except Exception:
        print("Invalid input. Please try again.")
    return album


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
