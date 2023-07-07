from unittest.mock import Mock

from album.app import run_app


def test_app_calls_prompt_for_album_until_return_value_not_none(monkeypatch):
    mock_prompt_for_album = Mock(side_effect=[None, None, 3])
    monkeypatch.setattr("album.service.prompt_for_album", mock_prompt_for_album)
    run_app()
    assert mock_prompt_for_album.call_count == 3


def test_app_calls_request_photos_with_album_id(monkeypatch):
    expected_album_id = 4
    mock_request_photos = Mock(return_value=[])
    monkeypatch.setattr("album.service.request_photos", mock_request_photos)
    monkeypatch.setattr("album.service.prompt_for_album", lambda: expected_album_id)
    monkeypatch.setattr("album.service.prompt_for_new_album", Mock())
    run_app()
    mock_request_photos.assert_called_once_with(expected_album_id)


def test_app_calls_print_photo_album_with_album_and_photos_returned_from_request_photos(monkeypatch):
    photos = [{"id": "1", "title": "photo1"}, {"id": "2", "title": "photo2"}]
    expected_album_id = 56
    monkeypatch.setattr("album.service.request_photos", lambda x: photos)
    monkeypatch.setattr("album.service.prompt_for_album", lambda: expected_album_id)
    mock_print_photo_album = Mock()
    monkeypatch.setattr("album.service.print_photo_album", mock_print_photo_album)
    run_app()
    mock_print_photo_album.assert_called_once_with(expected_album_id, photos)


def test_app_prints_error_if_photos_size_is_zero(monkeypatch, capsys):
    monkeypatch.setattr("album.service.request_photos", lambda x: [])
    monkeypatch.setattr("album.service.prompt_for_album", lambda: 65)
    monkeypatch.setattr("album.service.prompt_for_new_album", Mock())
    run_app()
    prompt = capsys.readouterr()
    assert "Error" in prompt.out


def test_app_calls_prompt_for_new_album_if_photos_size_is_zero(monkeypatch):
    mock_prompt_for_new_album = Mock()
    monkeypatch.setattr("album.service.prompt_for_new_album", mock_prompt_for_new_album)
    monkeypatch.setattr("album.service.request_photos", lambda x: [])
    monkeypatch.setattr("album.service.prompt_for_album", lambda: 65)
    run_app()
    mock_prompt_for_new_album.assert_called_once()
