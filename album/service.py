def prompt_for_album():
    album = None
    try:
        album = int(input("Please enter the ID of the photo album you would like to view content for: "))
    except Exception:
        print("Invalid input. Please try again.")
    return album


def request_photos(album_id: int):
    return