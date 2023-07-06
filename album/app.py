def prompt_for_album():
    try:
        album = int(input("Please enter the ID of the photo album you would like to view content for: "))
        return album
    except Exception:
        print("Invalid input. Please try again.")
