from album import service


def run_app():
    album = None
    while album is None:
        album = service.prompt_for_album()
    photos = service.request_photos(album)
    print(f"\nPhoto album {album} contains the following photos:")
    for photo in photos:
        print(f"\t{photo['id']}: {photo['title']}")
