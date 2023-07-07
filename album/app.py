from album import service


def run_app():
    album = None
    while album is None:
        album = service.prompt_for_album()
    service.request_photos(album)