from album import service


def run_app():
    album = None
    while album is None:
        album = service.prompt_for_album()
    photos = service.request_photos(album)
    service.print_photo_album(album, photos)
