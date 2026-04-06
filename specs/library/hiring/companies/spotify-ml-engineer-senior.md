---
kind: hiring
role: Senior ML Engineer
team: Personalization
level: L5
company: Spotify
version: 1
---

# What We're Looking For

I've been at Spotify for six years, and I can tell you that personalization here is fundamentally different from recommendation systems at other companies. We're not just optimizing for clicks or engagement time — we're trying to understand the emotional context of when someone needs music. The difference between what you want to hear at 7am vs 11pm vs during a workout isn't just genre preference, it's human psychology expressed through audio.

Our squad owns the entire personalization pipeline from feature engineering through model serving, but you'll be collaborating with squads across Discovery, Content Understanding, and Audio Intelligence. You need to think in systems, not just models. A 2% improvement in recommendation accuracy means nothing if it takes 500ms longer to serve, because our users will bounce before the track loads.

The best ML engineers I've hired here have strong opinions about the intersection of user experience and algorithmic design. If you've only worked on batch prediction systems, this might not be the right fit. We serve 500M+ users in real-time, and your models need to degrade gracefully when the content graph changes or when new artists upload tracks with zero listening history.

## Must-Haves

- Production recommendation systems experience with real-time serving constraints (<100ms p95 latency)
- Deep understanding of embedding techniques for sparse, cold-start problems (new tracks/artists)
- Experience with A/B testing methodology for ML systems where user behavior changes the data distribution
- Can articulate why collaborative filtering breaks down at Spotify's scale and what you'd use instead
- Hands-on experience with feature stores or similar ML infrastructure for managing temporal features

## Strong Signals

- Has worked with audio/music data or other high-dimensional creative content
- Experience with multi-armed bandits or other online learning approaches
- Can explain the difference between optimizing for discovery vs satisfaction in recommender systems
- Understanding of privacy-preserving ML techniques (we care about user privacy)
- Previous experience in autonomous squad environments where you owned ML products end-to-end

## Anti-Patterns

- ML experience limited to computer vision or NLP without understanding of recommendation systems
- Thinks personalization is just matrix factorization scaled up
- Can't explain how they'd handle the cold start problem for new users or new content
- Treats ML as a black box optimization problem without considering user experience
- Has only worked with clean, pre-processed datasets (our data is messy and streaming)

## Interview Focus

- Cold start scenarios: how would you recommend music to a user with zero listening history?
- System design: architecting real-time recommendation serving with fallback strategies
- Trade-offs between model complexity and inference speed in a mobile-first product
- A/B testing design for recommendation changes where user behavior affects future training data
- How they'd approach the explore/exploit problem when users have evolving music taste
