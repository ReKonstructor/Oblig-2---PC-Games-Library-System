"""
Game Model
Represents a single game in the library with properties like title, platform, and genre.
"""

import json
from datetime import datetime

class Game:
    """
    Represents a single game in the PC games library.
    
    Attributes:
        id (int): Unique identifier for the game
        title (str): Name of the game
        platform (str): Gaming platform (e.g., 'PC', 'Steam', 'Epic')
        genre (str): Game genre (e.g., 'RPG', 'Action', 'Strategy')
        is_favorite (bool): Whether the game is marked as favorite
        date_added (str): ISO format timestamp of when game was added
    """
    
    def __init__(self, title, platform="PC", genre="Uncategorized"):
        """
        Initialize a new Game instance.
        
        Args:
            title (str): The game's title
            platform (str, optional): The gaming platform. Defaults to "PC".
            genre (str, optional): The game's genre. Defaults to "Uncategorized".
        """
        self.id = None  # Will be set when saved
        self.title = title
        self.platform = platform
        self.genre = genre
        self.is_favorite = False
        self.date_added = datetime.now().isoformat()
    
    def toggle_favorite(self):
        """
        Toggle the favorite status of the game.
        
        Returns:
            bool: The new favorite status after toggling
        """
        self.is_favorite = not self.is_favorite
        return self.is_favorite
    
    def to_dict(self):
        """
        Convert game object to dictionary for JSON storage.
        
        Returns:
            dict: Dictionary representation of the game
        """
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
        """
        Create game object from dictionary.
        
        Args:
            data (dict): Dictionary containing game data
            
        Returns:
            Game: New Game instance created from the dictionary
        """
        game = cls(data['title'], data['platform'], data['genre'])
        game.id = data.get('id')
        game.is_favorite = data.get('is_favorite', False)
        game.date_added = data.get('date_added')
        return game


import requests

def import_game_from_steam(appid):
    """
    Import a game from the Steam API by AppID.
    
    Fetches game details including title, genre, and platform from Steam's
    public API and creates a Game object.
    
    Args:
        appid (int): The Steam Application ID
        
    Returns:
        Game: A new Game object with data from Steam, or None if import fails
        
    Example:
        >>> game = import_game_from_steam(570)  # Dota 2
        >>> print(game.title)
        'Dota 2'
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