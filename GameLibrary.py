import json

class GameLibrary:
    def __init__(self, filename="games.json"):
        self.filename = filename
        self.games = self.load_games()

    def load_games(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_games(self):
        with open(self.filename, "w") as f:
            json.dump(self.games, f, indent=2)

    def add_game(self, title, genre, platform="PC"):
        game = {"title": title, "genre": genre, "platform": platform}
        self.games.append(game)
        self.save_games()
        print(f"Added: {title}")

    def list_games(self):
        if not self.games:
            print("No games in library.")
            return
        for idx, game in enumerate(self.games, 1):
            print(f"{idx}. {game['title']} ({game['genre']}) - {game['platform']}")

    def remove_game(self, title):
        original_count = len(self.games)
        self.games = [g for g in self.games if g["title"].lower() != title.lower()]
        if len(self.games) < original_count:
            self.save_games()
            print(f"Removed: {title}")
        else:
            print(f"Game not found: {title}")

if __name__ == "__main__":
    lib = GameLibrary()
    while True:
        print("\n1. Add game\n2. List games\n3. Remove game\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Game title: ")
            genre = input("Genre: ")
            lib.add_game(title, genre)
        elif choice == "2":
            lib.list_games()
        elif choice == "3":
            title = input("Title to remove: ")
            lib.remove_game(title)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")