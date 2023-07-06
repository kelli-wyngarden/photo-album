from album import app


def test_prompt_for_album_prints_prompt(capsys):
    app.prompt_for_album()
    prompt = capsys.readouterr()
    assert "Please enter the ID of the photo album you would like to view content for: " in prompt.out
