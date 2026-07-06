# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

My version recommends songs by comparing each song's stored attributes to a
simple user taste profile. It focuses on content-based recommendation: instead
of looking at what similar listeners played, it checks whether a song's genre,
mood, energy, danceability, and acousticness match the user's stated
preferences.

---

## How The System Works

Real streaming platforms predict what a user might love next by connecting user
behavior data to song data. Collaborative filtering uses patterns from many
listeners, such as likes, skips, replays, playlist adds, follows, and listening
history, to find songs enjoyed by people with similar taste. Content-based
filtering looks at the song itself, such as genre, mood, tempo, energy, valence,
danceability, acousticness, lyrics, or audio features. My smaller simulator will
prioritize content-based filtering because the CSV already describes the songs.
For me, a musical "vibe" is mostly shaped by genre, mood, energy, tempo, and
acousticness, so those features make sense as the main signals.

The starting CSV had 10 songs, and I expanded it to 18 songs so the catalog has
more variety. The added songs include worldbeat, punk, R&B, electronic, folk,
soul, dream pop, and hip hop, with moods like adventurous, rebellious, romantic,
playful, nostalgic, warm, dreamy, and confident.

Specific features in this simulation:

- `Song`: `id`, `title`, `artist`, `genre`, `mood`, `energy`, `tempo_bpm`,
  `valence`, `danceability`, and `acousticness`
- `UserProfile`: `favorite_genre`, `favorite_mood`, `target_energy`,
  `target_danceability`, and `likes_acoustic`

Example user profile:

```python
user_prefs = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.80,
    "target_danceability": 0.80,
    "likes_acoustic": False,
}
```

This profile should separate "intense rock" from "chill lofi" because it uses
both category matches and numerical vibe matches. A loud rock song may be close
in energy, but it loses points if the genre and mood do not match. A chill lofi
song may be pleasant, but it is much farther from the target energy and mood.

Algorithm recipe:

- Add `2.0` points when the song's `genre` matches the user's
  `favorite_genre`.
- Add `1.5` points when the song's `mood` matches the user's `favorite_mood`.
- Add up to `1.0` point for `energy` closeness using
  `1 - abs(song_energy - target_energy)`.
- Add up to `0.5` points for `danceability` closeness using
  `0.5 * (1 - abs(song_danceability - target_danceability))`.
- Add `0.5` points when `likes_acoustic` matches the song's acousticness:
  acoustic fans get the bonus for songs at `0.60` or above, and non-acoustic
  fans get the bonus for songs below `0.60`.
- Sort all songs by total score from highest to lowest, then recommend the top
  `k` songs.

The scoring rule answers "how well does this one song match this one user?" The
ranking rule answers "after every song has a score, which songs should appear
first?" A recommender needs both: scoring creates the evidence for each song,
and ranking turns those scores into an ordered recommendation list.

Data flow:

```text
Input: user preferences
  -> Process: load each CSV row as a song
  -> Process: loop through every song and calculate its score
  -> Process: sort songs from highest score to lowest score
  -> Output: top k recommended songs with short explanations
```

Expected bias: this system may over-prioritize genre and mood labels, so it
could miss songs that have the right musical feel but use a different label. It
also depends on hand-picked weights, which means my assumptions decide what
counts as a good recommendation.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```
Loaded songs: 18

User profile:
  genre=pop, mood=happy, energy=0.80, danceability=0.80, likes_acoustic=False

Top recommendations:

1. Sunrise City by Neon Echo (pop, happy)
   Score: 5.48
   Because: genre match (+2.0); mood match (+1.5); energy closeness (+0.98); danceability closeness (+0.49); acoustic preference match (+0.5)

2. Gym Hero by Max Pulse (pop, intense)
   Score: 3.83
   Because: genre match (+2.0); energy closeness (+0.87); danceability closeness (+0.46); acoustic preference match (+0.5)

3. Rooftop Lights by Indigo Parade (indie pop, happy)
   Score: 3.45
   Because: mood match (+1.5); energy closeness (+0.96); danceability closeness (+0.49); acoustic preference match (+0.5)

4. Pixel Parade by Bit Bloom (electronic, playful)
   Score: 1.94
   Because: energy closeness (+0.99); danceability closeness (+0.45); acoustic preference match (+0.5)

5. Night Drive Loop by Neon Echo (synthwave, moody)
   Score: 1.92
   Because: energy closeness (+0.95); danceability closeness (+0.46); acoustic preference match (+0.5)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
