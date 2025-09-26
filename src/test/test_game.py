import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.models.game import Game

class TestGame(unittest.TestCase):
    
    def setUp(self):
        """Set up test game"""
        self.game = Game("The Witcher 3", "Steam", "RPG")
    
    def test_game_creation(self):
        """Test that a game is created with correct attributes"""
        self.assertEqual(self.game.title, "The Witcher 3")
        self.assertEqual(self.game.platform, "Steam")
        self.assertEqual(self.game.genre, "RPG")
        self.assertFalse(self.game.is_favorite)
    
    def test_toggle_favorite(self):
        """Test Thisath's user story: marking games as favorite"""
        # Initially not favorite
        self.assertFalse(self.game.is_favorite)
        
        # Toggle to favorite
        result = self.game.toggle_favorite()
        self.assertTrue(result)
        self.assertTrue(self.game.is_favorite)
        
        # Toggle back
        result = self.game.toggle_favorite()
        self.assertFalse(result)
        self.assertFalse(self.game.is_favorite)
    
    def test_to_dict(self):
        """Test converting game to dictionary"""
        game_dict = self.game.to_dict()
        self.assertEqual(game_dict['title'], "The Witcher 3")
        self.assertEqual(game_dict['platform'], "Steam")
        self.assertEqual(game_dict['genre'], "RPG")

if __name__ == '__main__':
    unittest.main()