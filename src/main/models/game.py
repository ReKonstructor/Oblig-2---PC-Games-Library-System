import json
from datetime import datetime

class Game:
    def __init__(self, title, platform="PC", genre="Uncategorized"):
        self.id = None  # Will be set when saved
        self.title = title
        self.platform = platform
        self.genre = genre
        self.is_favorite = False
        self.date_added = datetime.now().isoformat()
    
    def toggle_favorite(self):
        """Toggle the favorite status of the game"""
        self.is_favorite = not self.is_favorite
        return self.is_favorite
    
    def to_dict(self):
        """Convert game object to dictionary for JSON storage"""
        return {
            'id': self.id,
            'title': self.title,
            'platform': self.platform,
            'genre': self.genre,
            'is_favorite': self.is_favorite,
            'date_added': self.date_added
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create game object from dictionary"""
        game = cls(data['title'], data['platform'], data['genre'])
        game.id = data.get('id')
        game.is_favorite = data.get('is_favorite', False)
        game.date_added = data.get('date_added')
        return game