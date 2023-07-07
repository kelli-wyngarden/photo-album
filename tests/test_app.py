from unittest.mock import Mock

from album.app import run_app


def test_app_calls_prompt_for_album_until_return_value_not_none(monkeypatch):
    mock_prompt_for_album = Mock(side_effect=[None, None, 3])
    monkeypatch.setattr("album.service.prompt_for_album", mock_prompt_for_album)
    run_app()
    assert mock_prompt_for_album.call_count == 3
