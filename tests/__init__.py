"""
Unit tests for Hybrid Downloader.

License: MIT
"""

import pytest
from pathlib import Path
from hybrid_downloader.types import Type, Format, Quality
from hybrid_downloader.utils import sanitize_path, is_valid_spotify_url, check_ffmpeg, check_spotify_credentials
from hybrid_downloader.exceptions import InvalidURLError


class TestTypes:
    """Test type definitions."""
    
    def test_track_type(self):
        assert Type.TRACK == 'track'
    
    def test_album_type(self):
        assert Type.ALBUM == 'album'
    
    def test_playlist_type(self):
        assert Type.PLAYLIST == 'playlist'
    
    def test_artist_type(self):
        assert Type.ARTIST == 'artist'
    
    def test_mp3_format(self):
        assert Format.MP3 == 'mp3'
    
    def test_flac_format(self):
        assert Format.FLAC == 'flac'
    
    def test_quality_best(self):
        assert Quality.BEST == '0'
    
    def test_quality_320k(self):
        assert Quality.Q320K == '320'


class TestUtils:
    """Test utility functions."""
    
    def test_sanitize_path_removes_invalid_chars(self):
        result = sanitize_path('Song<Name>|Invalid')
        assert '<' not in result
        assert '>' not in result
        assert '|' not in result
    
    def test_sanitize_path_preserves_spaces(self):
        result = sanitize_path('Artist - Song Name')
        assert result == 'Artist - Song Name'
    
    def test_sanitize_path_removes_trailing_dots(self):
        result = sanitize_path('Song Name...')
        assert not result.endswith('.')
    
    def test_is_valid_spotify_url_with_https(self):
        url = 'https://open.spotify.com/track/123'
        assert is_valid_spotify_url(url)
    
    def test_is_valid_spotify_url_with_uri(self):
        url = 'spotify:track:123'
        assert is_valid_spotify_url(url)
    
    def test_is_valid_spotify_url_invalid(self):
        url = 'https://youtube.com/watch?v=123'
        assert not is_valid_spotify_url(url)
    
    def test_is_valid_spotify_url_playlist(self):
        url = 'https://open.spotify.com/playlist/abc'
        assert is_valid_spotify_url(url)
    
    def test_is_valid_spotify_url_artist(self):
        url = 'https://open.spotify.com/artist/xyz'
        assert is_valid_spotify_url(url)
    
    def test_check_ffmpeg_returns_bool(self):
        result = check_ffmpeg()
        assert isinstance(result, bool)
    
    def test_check_spotify_credentials_returns_bool(self):
        result = check_spotify_credentials()
        assert isinstance(result, bool)


class TestExceptions:
    """Test exception handling."""
    
    def test_invalid_url_error_contains_url(self):
        url = 'https://example.com/invalid'
        error = InvalidURLError(url)
        assert url in str(error)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
