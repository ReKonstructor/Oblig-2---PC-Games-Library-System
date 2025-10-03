#!/usr/bin/env python3
"""
PC Games Library System - CLI Version
A simple command-line interface for managing your game library
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.models.game_library import GameLibrary

class GameLibraryCLI:
    def __init__(self):
        self.library = GameLibrary("my_games.json")
        self.running = True
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("🎮 PC GAMES LIBRARY SYSTEM 🎮")
        print("="*50)
        print("1. Add a new game")
        print("2. View all games")
        print("3. View favorite games")
        print("4. Toggle favorite status")
        print("5. Filter games by genre")
        print("6. Remove a game")
        print("7. View all genres")
        print("8. Exit")
        print("="*50)
    
    def add_game(self):
        """Add a new game to the library"""
        print("\n--- Add New Game ---")
        title = input("Enter game title: ").strip()
        if not title:
            print("❌ Title cannot be empty!")
            return
        
        platform = input("Enter platform (default: PC): ").strip() or "PC"
        genre = input("Enter genre (default: Uncategorized): ").strip() or "Uncategorized"
        
        game = self.library.add_game(title, platform, genre)
        print(f"✅ Added: {game.title} (ID: {game.id})")
    
    def view_all_games(self):
        """Display all games in the library"""
        games = self.library.get_all_games()
        if not games:
            print("\n📚 No games in library yet.")
            return
        
        print("\n--- All Games ---")
        for game in games:
            fav = "⭐" if game.is_favorite else "  "
            print(f"{fav} [{game.id}] {game.title} ({game.genre}) - {game.platform}")
    
    def view_favorite_games(self):
        """Display only favorite games"""
        favorites = self.library.get_favorite_games()
        if not favorites:
            print("\n⭐ No favorite games yet.")
            return
        
        print("\n--- Favorite Games ---")
        for game in favorites:
            print(f"⭐ [{game.id}] {game.title} ({game.genre}) - {game.platform}")
    
    def toggle_favorite(self):
        """Toggle favorite status of a game"""
        self.view_all_games()
        if not self.library.games:
            return
        
        try:
            game_id = int(input("\nEnter game ID to toggle favorite: "))
            if self.library.toggle_favorite(game_id):
                game = self.library.get_game_by_id(game_id)
                status = "favorite" if game.is_favorite else "not favorite"
                print(f"✅ {game.title} is now {status}")
            else:
                print("❌ Game not found!")
        except ValueError:
            print("❌ Invalid ID!")
    
    def filter_by_genre(self):
        """Filter and display games by genre"""
        genres = self.library.get_genres()
        if not genres:
            print("\n📚 No games in library yet.")
            return
        
        print("\nAvailable genres:", ", ".join(genres))
        genre = input("Enter genre to filter: ").strip()
        
        games = self.library.get_games_by_genre(genre)
        if not games:
            print(f"No games found in genre: {genre}")
            return
        
        print(f"\n--- Games in {genre} genre ---")
        for game in games:
            fav = "⭐" if game.is_favorite else "  "
            print(f"{fav} [{game.id}] {game.title} - {game.platform}")
    
    def remove_game(self):
        """Remove a game from the library"""
        self.view_all_games()
        if not self.library.games:
            return
        
        try:
            game_id = int(input("\nEnter game ID to remove: "))
            game = self.library.get_game_by_id(game_id)
            if game and self.library.remove_game(game_id):
                print(f"✅ Removed: {game.title}")
            else:
                print("❌ Game not found!")
        except ValueError:
            print("❌ Invalid ID!")
    
    def view_genres(self):
        """Display all unique genres"""
        genres = self.library.get_genres()
        if not genres:
            print("\n📚 No genres yet.")
            return
        
        print("\n--- Available Genres ---")
        for genre in genres:
            count = len(self.library.get_games_by_genre(genre))
            print(f"• {genre} ({count} games)")
    
    def run(self):
        """Main application loop"""
        print("Welcome to PC Games Library System!")
        
        while self.running:
            self.display_menu()
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == "1":
                self.add_game()
            elif choice == "2":
                self.view_all_games()
            elif choice == "3":
                self.view_favorite_games()
            elif choice == "4":
                self.toggle_favorite()
            elif choice == "5":
                self.filter_by_genre()
            elif choice == "6":
                self.remove_game()
            elif choice == "7":
                self.view_genres()
            elif choice == "8":
                print("\n👋 Goodbye! Thanks for using PC Games Library System!")
                self.running = False
            else:
                print("❌ Invalid choice! Please enter 1-8.")

if __name__ == "__main__":
    app = GameLibraryCLI()
    app.run()