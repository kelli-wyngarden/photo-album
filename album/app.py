import service


def run_app():
    album = None
    while album is None:
        album = service.prompt_for_album()
    photos = service.request_photos(album)
    if len(photos) > 0:
        service.print_photo_album(album, photos)
    else:
        print("Error")
    service.prompt_for_new_album()


if __name__ == "__main__":
    run_app()
