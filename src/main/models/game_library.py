import json
import os
from typing import List, Optional
from .game import Game

class GameLibrary:
    def __init__(self, filename="games_library.json"):
        self.filename = filename
        self.games: List[Game] = []
        self.next_id = 1
        self.load_games()
    
    def load_games(self):
        """Load games from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.games = [Game.from_dict(game_data) for game_data in data.get('games', [])]
                    self.next_id = data.get('next_id', 1)
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading games: {e}")
                self.games = []
    
    def save_games(self):
        """Save games to JSON file"""
        data = {
            'games': [game.to_dict() for game in self.games],
            'next_id': self.next_id
        }
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_game(self, title: str, platform: str = "PC", genre: str = "Uncategorized") -> Game:
        """Add a new game to the library"""
        game = Game(title, platform, genre)
        game.id = self.next_id
        self.next_id += 1
        self.games.append(game)
        self.save_games()
        return game
    
    def remove_game(self, game_id: int) -> bool:
        """Remove a game by ID"""
        original_count = len(self.games)
        self.games = [g for g in self.games if g.id != game_id]
        if len(self.games) < original_count:
            self.save_games()
            return True
        return False
    
    def get_game_by_id(self, game_id: int) -> Optional[Game]:
        """Get a game by ID"""
        for game in self.games:
            if game.id == game_id:
                return game
        return None
    
    def toggle_favorite(self, game_id: int) -> bool:
        """Toggle favorite status of a game"""
        game = self.get_game_by_id(game_id)
        if game:
            result = game.toggle_favorite()
            self.save_games()
            return result
        return False
    
    def get_games_by_genre(self, genre: str) -> List[Game]:
        """Get all games of a specific genre"""
        return [game for game in self.games if game.genre.lower() == genre.lower()]
    
    def get_favorite_games(self) -> List[Game]:
        """Get all favorite games"""
        return [game for game in self.games if game.is_favorite]
    
    def get_all_games(self) -> List[Game]:
        """Get all games in the library"""
        return self.games
    
    def get_genres(self) -> List[str]:
        """Get list of unique genres"""
        genres = set(game.genre for game in self.games)
        return sorted(list(genres))