import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
    target_danceability: float = 0.8


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs ranked by the user's taste profile."""
        return sorted(
            self.songs,
            key=lambda song: self._score_dataclass_song(user, song)[0],
            reverse=True,
        )[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song matches the user's taste profile."""
        score, reasons = self._score_dataclass_song(user, song)
        return f"Score {score:.2f}: " + "; ".join(reasons)

    def _score_dataclass_song(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "target_danceability": user.target_danceability,
            "likes_acoustic": user.likes_acoustic,
        }
        song_dict = {
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
            "danceability": song.danceability,
            "acousticness": song.acousticness,
        }
        return score_song(user_prefs, song_dict)


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    int_fields = {"id"}
    float_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            for field in int_fields:
                row[field] = int(row[field])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)

    print(f"Loaded songs: {len(songs)}")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences and return reasons."""
    score = 0.0
    reasons = []

    favorite_genre = user_prefs.get("favorite_genre", user_prefs.get("genre", ""))
    favorite_mood = user_prefs.get("favorite_mood", user_prefs.get("mood", ""))
    target_energy = float(user_prefs.get("target_energy", user_prefs.get("energy", 0.5)))
    target_danceability = float(
        user_prefs.get("target_danceability", user_prefs.get("danceability", 0.8))
    )
    likes_acoustic = bool(user_prefs.get("likes_acoustic", False))

    if song["genre"].lower() == favorite_genre.lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"].lower() == favorite_mood.lower():
        score += 1.5
        reasons.append("mood match (+1.5)")

    energy_points = max(0.0, 1 - abs(float(song["energy"]) - target_energy))
    score += energy_points
    reasons.append(f"energy closeness (+{energy_points:.2f})")

    danceability_points = 0.5 * max(
        0.0,
        1 - abs(float(song["danceability"]) - target_danceability),
    )
    score += danceability_points
    reasons.append(f"danceability closeness (+{danceability_points:.2f})")

    is_acoustic = float(song["acousticness"]) >= 0.60
    if is_acoustic == likes_acoustic:
        score += 0.5
        reasons.append("acoustic preference match (+0.5)")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top k explained recommendations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, "; ".join(reasons)))

    return sorted(scored_songs, key=lambda item: item[1], reverse=True)[:k]
