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


# Function to import a game from the Steam API
import requests

def import_game_from_steam(appid):
    """
    Import a game from the Steam API by appid.
    Returns a Game object or None if not found.
    """
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if not data or not data.get(str(appid), {}).get('success'):
            return None
        game_data = data[str(appid)]['data']
        title = game_data.get('name', f"Steam App {appid}")
        genres = game_data.get('genres', [])
        genre = genres[0]['description'] if genres else "Uncategorized"
        platforms = game_data.get('platforms', {})
        platform = ", ".join([k.capitalize() for k, v in platforms.items() if v]) or "PC"
        return Game(title=title, platform=platform, genre=genre)
    except Exception as e:
        print(f"Error importing from Steam: {e}")
        return None