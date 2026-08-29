"""
Integration tests for Hybrid Downloader.

License: MIT
"""

import pytest
from hybrid_downloader.spotify_api import SpotifyAPI, Track
from hybrid_downloader.exceptions import SpotifyCredentialsError, InvalidURLError
from hybrid_downloader.types import Type


class TestSpotifyAPI:
    """Test Spotify API wrapper."""
    
    def test_track_creation(self):
        """Test Track object creation with minimal data."""
        track_data = {
            'id': 'test_id',
            'name': 'Test Song',
            'artists': [{'name': 'Test Artist'}],
            'album': {'name': 'Test Album', 'images': []},
            'external_urls': {'spotify': 'https://spotify.com/track/test_id'},
        }
        
        track = Track(track_data)
        
        assert track.id == 'test_id'
        assert track.name == 'Test Song'
        assert track.artists == ['Test Artist']
        assert track.album_name == 'Test Album'
        assert str(track) == 'Test Artist - Test Song'
    
    def test_track_with_missing_artists(self):
        """Test Track with missing artists field."""
        track_data = {
            'id': 'test_id',
            'name': 'Test Song',
            'album': {'name': 'Test Album', 'images': []},
            'external_urls': {'spotify': 'https://spotify.com/track/test_id'},
        }
        
        track = Track(track_data)
        assert track.artists == ['Unknown Artist']
    
    def test_track_string_representation(self):
        """Test Track string representation."""
        track_data = {
            'id': 'test_id',
            'name': 'Test Song',
            'artists': [{'name': 'Artist 1'}, {'name': 'Artist 2'}],
            'album': {'name': 'Test Album', 'images': []},
            'external_urls': {'spotify': 'https://spotify.com/track/test_id'},
        }
        
        track = Track(track_data)
        assert 'Artist 1' in str(track)
        assert 'Test Song' in str(track)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
