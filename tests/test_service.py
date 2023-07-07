from unittest.mock import Mock

from album import service


def test_prompt_for_album_prints_prompt(capsys):
    service.prompt_for_album()
    prompt = capsys.readouterr()
    assert "Please enter the ID of the photo album you would like to view content for: " in prompt.out


def test_prompt_for_album_prints_error_if_input_is_string(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: "three")
    service.prompt_for_album()
    prompt = capsys.readouterr()
    assert "Invalid input. Please try again." in prompt.out


def test_prompt_for_album_returns_value_if_input_is_int(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: "3")
    result = service.prompt_for_album()
    assert result == 3


def test_request_photos_makes_get_call_with_url_and_album_id(monkeypatch):
    album_id = 12
    expected_url = "https://jsonplaceholder.typicode.com/photos"
    mock_requests = Mock()
    monkeypatch.setattr("requests.get", mock_requests)
    service.request_photos(album_id)
    mock_requests.assert_called_once_with(expected_url, params={"albumId": album_id})
