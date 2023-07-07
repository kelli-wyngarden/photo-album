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
    run_app()
    mock_request_photos.assert_called_once_with(expected_album_id)


def test_app_prints_photos_returned_from_request_photos(monkeypatch, capsys):
    photos = [{"id": "1", "title": "photo1"}, {"id": "2", "title": "photo2"}]
    monkeypatch.setattr("album.service.request_photos", lambda x: photos)
    monkeypatch.setattr("album.service.prompt_for_album", lambda: 56)
    run_app()
    prompt = capsys.readouterr()
    assert "Photo album 56 contains the following photos:" in prompt.out
    assert "1: photo1" in prompt.out
    assert "2: photo2" in prompt.out
