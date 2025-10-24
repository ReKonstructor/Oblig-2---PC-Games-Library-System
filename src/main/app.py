#!/usr/bin/env python3
"""
PC Games Library System - Flask Web Application
Web interface for managing game library
"""

import sys
import os
from flask import Flask, render_template, request, redirect, url_for, flash
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.models.game_library import GameLibrary

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages
library = GameLibrary("my_games.json")

@app.route('/')
def index():
    """Home page with list of all games"""
    games = library.get_all_games()
    return render_template('index.html', games=games)

@app.route('/add', methods=['GET', 'POST'])
def add_game():
    """Add a new game"""
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        if not title:
            flash('Title is required!', 'error')
            return redirect(url_for('add_game'))
        
        platform = request.form.get('platform', 'PC').strip()
        genre = request.form.get('genre', 'Uncategorized').strip()
        
        game = library.add_game(title, platform, genre)
        flash(f'Added: {game.title}', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_game.html')

@app.route('/favorites')
def favorites():
    """Show favorite games"""
    games = library.get_favorite_games()
    return render_template('favorites.html', games=games)

@app.route('/toggle-favorite/<int:game_id>')
def toggle_favorite(game_id):
    """Toggle favorite status of a game"""
    if library.toggle_favorite(game_id):
        game = library.get_game_by_id(game_id)
        status = "marked as favorite" if game.is_favorite else "unmarked as favorite"
        flash(f'{game.title} {status}', 'success')
    else:
        flash('Game not found', 'error')
    return redirect(request.referrer or url_for('index'))

@app.route('/genre/<genre>')
def games_by_genre(genre):
    """Show games filtered by genre"""
    games = library.get_games_by_genre(genre)
    genres = library.get_genres()
    return render_template('genre.html', genre=genre, games=games, genres=genres)

@app.route('/remove/<int:game_id>')
def remove_game(game_id):
    """Remove a game"""
    game = library.get_game_by_id(game_id)
    if game and library.remove_game(game_id):
        flash(f'Removed: {game.title}', 'success')
    else:
        flash('Game not found', 'error')
    return redirect(url_for('index'))
        
if __name__ == "__main__":
    app.run(debug=True)