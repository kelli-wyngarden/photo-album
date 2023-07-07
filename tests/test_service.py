from unittest.mock import Mock

import pytest
import requests.exceptions
from requests import Response

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


def test_request_photos_returns_response_json(monkeypatch):
    expected_return = [{"id": "1", "title": "photo1"}, {"id": "2", "title": "photo2"}]
    response = Response()
    response.json = Mock(return_value=expected_return)
    mock_requests = Mock(return_value=response)
    monkeypatch.setattr("requests.get", mock_requests)
    result = service.request_photos(34)
    assert result == expected_return


def test_request_photos_returns_empty_list_if_exception_raised(monkeypatch):
    mock_requests = Mock(side_effect=requests.exceptions.RequestException)
    monkeypatch.setattr("requests.get", mock_requests)
    result = service.request_photos(34)
    assert result == []


def test_print_photo_album_prints_photos(capsys):
    photos = [{"id": "1", "title": "photo1"}, {"id": "2", "title": "photo2"}]
    album_id = 42
    service.print_photo_album(album_id, photos)
    prompt = capsys.readouterr()
    assert f"Photo album {album_id} contains the following photos:" in prompt.out
    assert f"{photos[0]['id']}: {photos[0]['title']}" in prompt.out
    assert f"{photos[1]['id']}: {photos[1]['title']}" in prompt.out


def test_prompt_for_new_album_prints_invalid_input_if_not_y_n_yes_or_no(capsys, monkeypatch):
    mock_input = Mock(side_effect=["nope", "y"])
    monkeypatch.setattr("builtins.input", mock_input)
    monkeypatch.setattr("album.app.run_app", Mock())
    service.prompt_for_new_album()
    prompt = capsys.readouterr()
    assert "Invalid input." in prompt.out


def test_prompt_for_new_album_calls_run_app_if_input_yes(monkeypatch):
    mock_run_app = Mock()
    monkeypatch.setattr("album.app.run_app", mock_run_app)
    monkeypatch.setattr("builtins.input", lambda x: "Y")
    service.prompt_for_new_album()
    mock_run_app.assert_called_once()


def test_prompt_for_new_album_exits_if_input_no(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: "n")
    with pytest.raises(SystemExit):
        service.prompt_for_new_album()
