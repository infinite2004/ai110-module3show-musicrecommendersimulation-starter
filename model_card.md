# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder CLI 1.0**

---

## 2. Intended Use

This recommender is designed for classroom exploration, not real music users. It
generates a ranked list of songs from a small CSV catalog by comparing each song
to a user taste profile. It assumes the user can describe their taste with a few
simple preferences: genre, mood, target energy, target danceability, and whether
they like acoustic songs.

---

## 3. How the Model Works

The model uses content-based recommendation. It does not learn from other
listeners. Instead, it looks at the features already stored for each song:
genre, mood, energy, tempo, valence, danceability, and acousticness.

Each song receives points for matching the user's preferences. A genre match
adds 2.0 points, a mood match adds 1.5 points, energy closeness adds up to 1.0
point, danceability closeness adds up to 0.5 points, and acoustic preference can
add 0.5 points. After every song gets a score, the recommender sorts the songs
from highest score to lowest score and prints the top 5 with explanations.

---

## 4. Data

The catalog has 18 songs. The starter file had 10 songs, and I added 8 more to
include more variety: worldbeat, punk, R&B, electronic, folk, soul, dream pop,
and hip hop. The dataset includes useful musical vibe features, but it is still
missing lyrics, language, release year, artist popularity, listening history,
and user feedback such as likes, skips, and playlist adds.

---

## 5. Strengths

The system works best when the user profile has clear, non-conflicting signals.
For example, the pop/happy profile correctly ranks "Sunrise City" first because
it matches both the genre and mood while also being close in energy and
danceability. The lofi/chill profile also feels accurate because it puts the
lofi and chill tracks at the top before moving to nearby relaxed/acoustic songs.

The explanations are a strength because they show exactly why a song appeared.
For a non-programmer, the result is not just "the computer picked this song";
the CLI says whether the recommendation came from genre, mood, energy, dancing
feel, or acousticness.

---

## 6. Limitations and Bias

One weakness is that the genre score is powerful enough to create a small filter
bubble. In the adversarial "Sad Workout" profile, "Quiet Porch" ranks first in
the baseline because it matches `folk`, even though its energy is much lower
than the user requested. This means the system can over-prioritize labels and
ignore songs that fit the actual activity better.

The catalog is also tiny, so one song can look like the "best" answer just
because there are not many alternatives. The system does not understand lyrics,
artist similarity, listening context, or whether the user is tired of hearing
the same artist. It may also treat broad labels like "pop" or "chill" as more
important than subtle musical similarities.

---

## 7. Evaluation

I tested four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and an
adversarial profile called Sad Workout. I looked for whether the top songs
matched the user's stated genre and mood, whether the energy level felt right,
and whether any surprising songs appeared near the top.

### High-Energy Pop

```text
Loaded songs: 18

=== High-Energy Pop ===
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

"Sunrise City" ranked first because it matched every major signal: pop genre,
happy mood, high-but-not-too-high energy, strong danceability, and low
acousticness. "Gym Hero" keeps showing up for a happy pop listener because it is
pop and energetic, even though its mood is intense instead of happy.

### Chill Lofi

```text
=== Chill Lofi ===
User profile:
  genre=lofi, mood=chill, energy=0.35, danceability=0.60, likes_acoustic=True

Top recommendations:

1. Library Rain by Paper Lanterns (lofi, chill)
   Score: 5.49
   Because: genre match (+2.0); mood match (+1.5); energy closeness (+1.00); danceability closeness (+0.49); acoustic preference match (+0.5)

2. Midnight Coding by LoRoom (lofi, chill)
   Score: 5.42
   Because: genre match (+2.0); mood match (+1.5); energy closeness (+0.93); danceability closeness (+0.49); acoustic preference match (+0.5)

3. Focus Flow by LoRoom (lofi, focused)
   Score: 3.95
   Because: genre match (+2.0); energy closeness (+0.95); danceability closeness (+0.50); acoustic preference match (+0.5)

4. Spacewalk Thoughts by Orbit Bloom (ambient, chill)
   Score: 3.33
   Because: mood match (+1.5); energy closeness (+0.93); danceability closeness (+0.41); acoustic preference match (+0.5)

5. Coffee Shop Stories by Slow Stereo (jazz, relaxed)
   Score: 1.95
   Because: energy closeness (+0.98); danceability closeness (+0.47); acoustic preference match (+0.5)
```

This output feels right because low-energy, acoustic, chill songs rise to the
top. Compared with High-Energy Pop, the ranking shifts away from dance-pop and
toward quiet songs because the target energy is lower and `likes_acoustic` is
true.

### Deep Intense Rock

```text
=== Deep Intense Rock ===
User profile:
  genre=rock, mood=intense, energy=0.92, danceability=0.65, likes_acoustic=False

Top recommendations:

1. Storm Runner by Voltline (rock, intense)
   Score: 5.49
   Because: genre match (+2.0); mood match (+1.5); energy closeness (+0.99); danceability closeness (+0.49); acoustic preference match (+0.5)

2. Gym Hero by Max Pulse (pop, intense)
   Score: 3.38
   Because: mood match (+1.5); energy closeness (+0.99); danceability closeness (+0.39); acoustic preference match (+0.5)

3. Basement Sparks by Static Harbor (punk, rebellious)
   Score: 1.94
   Because: energy closeness (+0.96); danceability closeness (+0.48); acoustic preference match (+0.5)

4. Sunrise City by Neon Echo (pop, happy)
   Score: 1.83
   Because: energy closeness (+0.90); danceability closeness (+0.43); acoustic preference match (+0.5)

5. Night Drive Loop by Neon Echo (synthwave, moody)
   Score: 1.79
   Because: energy closeness (+0.83); danceability closeness (+0.46); acoustic preference match (+0.5)
```

This profile strongly prefers "Storm Runner," which makes sense because it is
both rock and intense. Compared with Chill Lofi, the output flips from quiet
acoustic tracks to high-energy non-acoustic tracks. Compared with High-Energy
Pop, "Gym Hero" is still relevant because it shares the intense/high-energy
signals even though it is pop instead of rock.

### Adversarial Sad Workout

```text
=== Adversarial Sad Workout ===
User profile:
  genre=folk, mood=intense, energy=0.90, danceability=0.85, likes_acoustic=True

Top recommendations:

1. Quiet Porch by Willow Frame (folk, nostalgic)
   Score: 3.22
   Because: genre match (+2.0); energy closeness (+0.41); danceability closeness (+0.31); acoustic preference match (+0.5)

2. Gym Hero by Max Pulse (pop, intense)
   Score: 2.95
   Because: mood match (+1.5); energy closeness (+0.97); danceability closeness (+0.48)

3. Storm Runner by Voltline (rock, intense)
   Score: 2.90
   Because: mood match (+1.5); energy closeness (+0.99); danceability closeness (+0.41)

4. Afterglow Drift by Cloud Atlas (dream pop, dreamy)
   Score: 1.43
   Because: energy closeness (+0.57); danceability closeness (+0.36); acoustic preference match (+0.5)

5. Midnight Coding by LoRoom (lofi, chill)
   Score: 1.41
   Because: energy closeness (+0.52); danceability closeness (+0.39); acoustic preference match (+0.5)
```

This profile was designed to be difficult because it asks for folk/acoustic
music but also intense, high-energy workout music. The surprising result is that
"Quiet Porch" wins because the genre match is worth 2.0 points. My intuition
says "Gym Hero" or "Storm Runner" fits the workout part better, so this exposed
that genre can dominate when preferences conflict.

### Sensitivity Experiment

I temporarily changed the scoring rule by halving genre from 2.0 to 1.0 and
doubling energy from a maximum of 1.0 to a maximum of 2.0. With that experiment,
the adversarial profile changed: "Gym Hero" ranked first, "Storm Runner" ranked
second, and "Quiet Porch" dropped to third. This made the workout profile feel
more accurate, but it also made the model more likely to recommend songs just
because their energy is close. I restored the original weights after the
experiment.

Pairwise comparisons:

- High-Energy Pop vs. Chill Lofi: pop prefers bright, energetic, low-acoustic
  songs, while lofi prefers low-energy acoustic songs.
- High-Energy Pop vs. Deep Intense Rock: both like energy, but rock shifts the
  top result toward intense guitar music instead of happy pop.
- Chill Lofi vs. Deep Intense Rock: the model clearly separates study music
  from workout-style music because energy, mood, and acousticness all point in
  different directions.
- Deep Intense Rock vs. Adversarial Sad Workout: both reward intensity, but the
  adversarial profile shows that a genre match can overpower the intended energy
  feel.

---

## 8. Future Work

I would add more songs and more user preferences, such as favorite artists,
tempo range, and whether the user wants familiar or surprising recommendations.
I would also add a diversity rule so the top 5 does not become too repetitive.
Another improvement would be making the weights adjustable from the command line
so the user can choose whether genre, mood, or energy matters most.

---

## 9. Personal Reflection

I learned that recommender systems are partly about scoring individual items and
partly about deciding which signals deserve the most power. A recommendation can
look mathematically correct but still feel wrong if the weights do not match the
real situation. The adversarial profile made that clear: "Quiet Porch" won by
the formula, but not by my intuition for workout music.
