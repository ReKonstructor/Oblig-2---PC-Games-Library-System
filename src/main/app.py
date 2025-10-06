#!/usr/bin/env python3
"""
PC Games Library System - MVP
Simple CLI for managing game library
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.models.game_library import GameLibrary

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print application header"""
    print("="*50)
    print("    🎮 PC GAMES LIBRARY SYSTEM MVP 🎮")
    print("="*50)

def main():
    library = GameLibrary("my_games.json")
    
    while True:
        print_header()
        print("\n1. Add Game")
        print("2. View All Games")
        print("3. View Favorite Games")
        print("4. Mark/Unmark as Favorite")
        print("5. Filter by Genre")
        print("6. Remove Game")
        print("7. Exit")
        print("\n" + "="*50)
        
        choice = input("\nSelect option (1-7): ")
        
        if choice == "1":
            # Add Game
            print("\n--- ADD NEW GAME ---")
            title = input("Title: ").strip()
            if not title:
                print("❌ Title required!")
                input("\nPress Enter to continue...")
                continue
            
            platform = input("Platform (default PC): ").strip() or "PC"
            genre = input("Genre (default Uncategorized): ").strip() or "Uncategorized"
            
            game = library.add_game(title, platform, genre)
            print(f"✅ Added: {game.title}")
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            # View All Games
            print("\n--- ALL GAMES ---")
            games = library.get_all_games()
            if not games:
                print("No games in library")
            else:
                for game in games:
                    star = "⭐" if game.is_favorite else ""
                    print(f"{star} [{game.id}] {game.title} - {game.genre} ({game.platform})")
            input("\nPress Enter to continue...")
            
        elif choice == "3":
            # View Favorites
            print("\n--- FAVORITE GAMES ---")
            favorites = library.get_favorite_games()
            if not favorites:
                print("No favorite games")
            else:
                for game in favorites:
                    print(f"⭐ [{game.id}] {game.title} - {game.genre} ({game.platform})")
            input("\nPress Enter to continue...")
            
        elif choice == "4":
            # Toggle Favorite
            games = library.get_all_games()
            if not games:
                print("\nNo games to mark as favorite")
                input("Press Enter to continue...")
                continue
                
            print("\n--- TOGGLE FAVORITE ---")
            for game in games:
                star = "⭐" if game.is_favorite else ""
                print(f"{star} [{game.id}] {game.title}")
            
            try:
                game_id = int(input("\nEnter game ID: "))
                if library.toggle_favorite(game_id):
                    game = library.get_game_by_id(game_id)
                    status = "marked as favorite ⭐" if game.is_favorite else "unmarked as favorite"
                    print(f"✅ {game.title} {status}")
                else:
                    print("❌ Game not found")
            except ValueError:
                print("❌ Invalid ID")
            input("\nPress Enter to continue...")
            
        elif choice == "5":
            # Filter by Genre
            genres = library.get_genres()
            if not genres:
                print("\nNo games in library")
                input("Press Enter to continue...")
                continue
                
            print("\n--- FILTER BY GENRE ---")
            print("Available genres:", ", ".join(genres))
            genre = input("Enter genre: ").strip()
            
            games = library.get_games_by_genre(genre)
            if games:
                print(f"\n{genre} Games:")
                for game in games:
                    star = "⭐" if game.is_favorite else ""
                    print(f"{star} [{game.id}] {game.title} ({game.platform})")
            else:
                print(f"No games in {genre}")
            input("\nPress Enter to continue...")
            
        elif choice == "6":
            # Remove Game
            games = library.get_all_games()
            if not games:
                print("\nNo games to remove")
                input("Press Enter to continue...")
                continue
                
            print("\n--- REMOVE GAME ---")
            for game in games:
                print(f"[{game.id}] {game.title}")
            
            try:
                game_id = int(input("\nEnter game ID to remove: "))
                game = library.get_game_by_id(game_id)
                if game and library.remove_game(game_id):
                    print(f"✅ Removed: {game.title}")
                else:
                    print("❌ Game not found")
            except ValueError:
                print("❌ Invalid ID")
            input("\nPress Enter to continue...")
            
        elif choice == "7":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid option")
            input("\nPress Enter to continue...")
        
        clear_screen()

if __name__ == "__main__":
    main()