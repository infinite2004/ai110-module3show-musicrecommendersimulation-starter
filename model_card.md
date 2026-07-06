# Model Card: VibeFinder CLI 1.0

## Model Name

**VibeFinder CLI 1.0**

## Goal / Task

This recommender suggests songs from a small CSV catalog. It tries to predict
which songs best match a user's music taste profile.

The system is a classroom simulation. It is meant to show how recommendation
logic works in a simple, explainable way.

## Data Used

The dataset has 18 songs. Each song has a title, artist, genre, mood, energy,
tempo, valence, danceability, and acousticness.

The starter file had 10 songs. I added 8 more songs to include more genres and
moods, such as punk, R&B, folk, soul, hip hop, dream pop, and electronic.

The dataset is still very small. It does not include lyrics, user listening
history, skips, likes, playlist adds, or artist popularity.

## Algorithm Summary

The recommender is content-based. It compares a user's preferences to each song.

The score works like this:

- Genre match: `+2.0`
- Mood match: `+1.5`
- Energy closeness: up to `+1.0`
- Danceability closeness: up to `+0.5`
- Acoustic preference match: `+0.5`

After scoring every song, the program sorts the songs from highest score to
lowest score. It prints the top 5 songs with reasons for each recommendation.

## Observed Behavior / Biases

The system works well when the user's preferences are clear. For example, a
happy pop profile correctly ranks "Sunrise City" first because it matches genre,
mood, energy, danceability, and acousticness.

The system struggles with conflicting preferences. In the "Adversarial Sad
Workout" profile, the user asks for folk/acoustic music but also high energy and
intense mood. "Quiet Porch" ranks first because it matches folk, even though it
is not a good workout song.

This shows a bias in the scoring logic. Genre can be too powerful, so the
system may create a small filter bubble around labels instead of musical feel.

## Evaluation Process

I tested four profiles:

- **High-Energy Pop:** pop, happy, high energy, danceable, not acoustic
- **Chill Lofi:** lofi, chill, low energy, medium danceability, acoustic
- **Deep Intense Rock:** rock, intense, very high energy, not acoustic
- **Adversarial Sad Workout:** folk, intense, high energy, danceable, acoustic

The clean profiles mostly behaved as expected. High-Energy Pop recommended
bright pop songs. Chill Lofi recommended low-energy lofi and ambient songs. Deep
Intense Rock recommended "Storm Runner" first, which made sense because it is
rock, intense, and very energetic.

The surprising result came from the adversarial profile. The top song matched
the genre but not the activity. I tested a temporary experiment where genre was
worth less and energy was worth more. That made "Gym Hero" and "Storm Runner"
rank higher, which felt better for a workout profile. I restored the original
weights after the experiment.

## Intended Use and Non-Intended Use

This project is intended for learning. It can help explain how a recommender
scores songs, ranks them, and gives reasons.

It should not be used as a real music recommendation system. It has too little
data, no real user behavior, and no way to learn from feedback over time.

It should also not be used to make serious decisions about artists, listeners,
or music quality. The output only reflects the small CSV and my hand-written
weights.

## Ideas for Improvement

- Add more songs so each genre and mood has better coverage.
- Let the user change weights for genre, mood, energy, and acousticness.
- Add feedback, such as likes, skips, or "play again," so the system can learn.
- Add a diversity rule so the top 5 does not feel repetitive.

## Personal Reflection

My biggest learning moment was seeing how much the weights matter. The system
looked logical on paper, but the adversarial profile showed that a simple rule
can still produce a weird result. "Quiet Porch" won because genre had a strong
score, even though it did not fit the workout vibe.

Using AI tools helped me brainstorm the scoring logic, generate extra songs,
write cleaner explanations, and compare the results across profiles. I still had
to double-check the outputs myself. The AI could suggest reasonable rules, but I
had to decide whether the recommendations actually felt right.

What surprised me most is that a simple algorithm can still feel like a real
recommendation system. Once the program prints a title, score, and reason, the
result feels intentional. That also made the limitations more obvious, because a
bad recommendation can sound confident if the explanation is too clean.

If I extended this project, I would make the user profile more flexible. I would
also add a way for the user to rate recommendations so the system could adjust
over time instead of using fixed weights forever.
