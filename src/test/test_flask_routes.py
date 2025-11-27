import unittest
import sys
import os
import json
import tempfile

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.app import app
from main.models.game_library import GameLibrary

class TestFlaskRoutes(unittest.TestCase):
    
    def setUp(self):
        """Set up test client and temporary database"""
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        
        # Create temporary file for test database
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        
    def tearDown(self):
        """Clean up temporary file"""
        try:
            os.unlink(self.temp_file.name)
        except:
            pass
    
    def test_index_route(self):
        """Test that index page loads"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Games Library', response.data)
    
    def test_add_game_get(self):
        """Test add game page loads"""
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add New Game', response.data)
    
    def test_add_game_post(self):
        """Test adding a game via POST"""
        response = self.client.post('/add', data={
            'title': 'Test Game',
            'platform': 'PC',
            'genre': 'Action'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Game', response.data)
    
    def test_add_game_empty_title(self):
        """Test that empty title shows error"""
        response = self.client.post('/add', data={
            'title': '',
            'platform': 'PC',
            'genre': 'Action'
        }, follow_redirects=True)
        self.assertIn(b'Title is required', response.data)
    
    def test_favorites_route(self):
        """Test favorites page loads"""
        response = self.client.get('/favorites')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Favorite Games', response.data)
    
    def test_import_steam_get(self):
        """Test Steam import page loads"""
        response = self.client.get('/import-steam')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Steam AppID', response.data)

if __name__ == '__main__':
    unittest.main()