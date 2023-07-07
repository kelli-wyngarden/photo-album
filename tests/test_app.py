from unittest.mock import Mock

from album.app import run_app


def test_app_calls_prompt_for_album_until_return_value_not_none(monkeypatch):
    mock_prompt_for_album = Mock(side_effect=[None, None, 3])
    monkeypatch.setattr("album.service.prompt_for_album", mock_prompt_for_album)
    run_app()
    assert mock_prompt_for_album.call_count == 3


def test_app_calls_request_photos_with_album_id(monkeypatch):
    expected_album_id = 4
    mock_request_photos = Mock()
    monkeypatch.setattr("album.service.request_photos", mock_request_photos)
    monkeypatch.setattr("album.service.prompt_for_album", lambda: expected_album_id)
    run_app()
    mock_request_photos.assert_called_once_with(expected_album_id)
