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
    
    def test_add_game(self):
        """Test Halvard's test: adding games to library"""
        game = self.library.add_game("Portal 2", "Steam", "Puzzle")
        self.assertEqual(game.title, "Portal 2")
        self.assertEqual(game.platform, "Steam")
        self.assertEqual(game.genre, "Puzzle")
        self.assertEqual(game.id, 1)
        self.assertEqual(len(self.library.games), 1)
    
    def test_remove_game(self):
        """Test removing games from library"""
        game = self.library.add_game("Half-Life 3", "Steam", "FPS")
        game_id = game.id
        
        # Remove the game
        result = self.library.remove_game(game_id)
        self.assertTrue(result)
        self.assertEqual(len(self.library.games), 0)
        
        # Try to remove non-existent game
        result = self.library.remove_game(999)
        self.assertFalse(result)
    
    def test_toggle_favorite_in_library(self):
        """Test toggling favorites through library"""
        game = self.library.add_game("Minecraft", "PC", "Sandbox")
        
        # Toggle to favorite
        result = self.library.toggle_favorite(game.id)
        self.assertTrue(result)
        
        # Check if game is in favorites
        favorites = self.library.get_favorite_games()
        self.assertEqual(len(favorites), 1)
        self.assertEqual(favorites[0].title, "Minecraft")
    
    def test_filter_by_genre(self):
        """Test filtering games by genre"""
        self.library.add_game("Dark Souls", "PC", "RPG")
        self.library.add_game("Elden Ring", "PC", "RPG")
        self.library.add_game("Tetris", "PC", "Puzzle")
        
        rpg_games = self.library.get_games_by_genre("RPG")
        self.assertEqual(len(rpg_games), 2)
        
        puzzle_games = self.library.get_games_by_genre("Puzzle")
        self.assertEqual(len(puzzle_games), 1)
    
    def test_persistence(self):
        """Test that games persist when library is reloaded"""
        # Add games
        game1 = self.library.add_game("Cyberpunk 2077", "PC", "RPG")
        self.library.toggle_favorite(game1.id)
        self.library.add_game("Hades", "PC", "Roguelike")
        
        # Create new library instance with same file
        library2 = GameLibrary(self.temp_file.name)
        
        # Check games are loaded
        self.assertEqual(len(library2.games), 2)
        self.assertEqual(library2.games[0].title, "Cyberpunk 2077")
        self.assertTrue(library2.games[0].is_favorite)
        self.assertEqual(library2.games[1].title, "Hades")

if __name__ == '__main__':
    unittest.main()