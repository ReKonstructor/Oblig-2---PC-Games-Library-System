import unittest
import sys
import os
import tempfile

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.models.game_library import GameLibrary
from main.models.game import Game

class TestGameLibrary(unittest.TestCase):
    
    def setUp(self):
        """Set up test library with temporary file"""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.library = GameLibrary(self.temp_file.name)
    
    def tearDown(self):
        """Clean up temporary file"""
        try:
            os.unlink(self.temp_file.name)
        except:
            pass
    
    def test_add_and_retrieve_game(self):
        """Test Halvard's test: adding and retrieving games"""
        # Add a game
        game = self.library.add_game("Portal 2", "Steam", "Puzzle")
        
        # Check it was added correctly
        self.assertEqual(game.title, "Portal 2")
        self.assertEqual(game.platform, "Steam")
        self.assertEqual(game.genre, "Puzzle")
        self.assertEqual(len(self.library.games), 1)
        
        # Check we can retrieve it
        retrieved = self.library.get_game_by_id(game.id)
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.title, "Portal 2")
    
    def test_favorite_games_filtering(self):
        """Test getting favorite games"""
        # Add some games
        game1 = self.library.add_game("Minecraft", "PC", "Sandbox")
        game2 = self.library.add_game("Terraria", "PC", "Sandbox")
        
        # Mark one as favorite
        self.library.toggle_favorite(game1.id)
        
        # Get favorites
        favorites = self.library.get_favorite_games()
        self.assertEqual(len(favorites), 1)
        self.assertEqual(favorites[0].title, "Minecraft")
    
    def test_genre_filtering(self):
        """Test filtering by genre"""
        # Add games with different genres
        self.library.add_game("Dark Souls", "PC", "RPG")
        self.library.add_game("Skyrim", "PC", "RPG")
        self.library.add_game("Tetris", "PC", "Puzzle")
        
        # Test filtering
        rpg_games = self.library.get_games_by_genre("RPG")
        self.assertEqual(len(rpg_games), 2)
        
        puzzle_games = self.library.get_games_by_genre("Puzzle")
        self.assertEqual(len(puzzle_games), 1)

if __name__ == '__main__':
    unittest.main()