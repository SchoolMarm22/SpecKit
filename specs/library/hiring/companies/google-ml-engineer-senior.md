---
kind: hiring
role: Senior ML Engineer
team: DeepMind / Core ML
level: L5
version: 1
---

# What We're Looking For

We're not just building ML models — we're building the infrastructure that powers intelligence at Google scale. Every line of code you write will potentially serve billions of users, which means different design constraints than most ML roles. Your models need to be fast, interpretable, and debuggable by oncall engineers at 3am.

This is deeply technical IC work. You'll spend weeks in design docs before touching code, and that's by design. We'd rather debate tensor shapes in a doc for two weeks than debug them in production for six months. If you've never written a 20-page design doc that got absolutely torn apart in review, this might not be the role for you.

The promo path here rewards technical depth and measurable impact on user-facing metrics. "I improved model accuracy by 2%" matters less than "I reduced serving latency by 20ms for 100M+ daily queries." We care about production systems, not research demos.

## Must-Haves

- Shipped production ML systems that serve >1M QPS (not batch jobs)
- Deep experience with distributed training frameworks (JAX/Flax preferred, but solid TensorFlow/PyTorch acceptable)
- Can articulate memory/compute tradeoffs in model architecture decisions
- Experience with model optimization for inference (quantization, pruning, knowledge distillation)
- Proficient with C++ for performance-critical components (Python is for prototyping)

## Strong Signals

- Has authored design docs that influenced team technical direction
- Experience with large-scale data pipelines (Flume, MapReduce, or equivalent)
- Understanding of hardware constraints (TPU characteristics, memory hierarchies)
- Can debug model training at scale (knows when it's a data issue vs. optimization vs. distributed systems)
- Track record of shipping features that moved business metrics

## Anti-Patterns

- Research background with no production experience ("it worked in Colab")
- Can't explain why their model architecture choices matter for serving
- Views code review as a formality rather than technical discourse
- Optimizes for paper metrics over user-facing impact
- Uncomfortable with the bureaucracy of large-scale engineering (design docs, launch reviews, etc.)

## Interview Focus

- System design: "How would you serve personalized recommendations to 1B+ users with <100ms p99 latency?"
- ML depth: Can they debug a training run that's not converging? Do they understand the math behind their architectural choices?
- Scale experience: Have they personally dealt with distributed systems failure modes?
- Code quality: Do they write code that other people can understand and maintain?
- Googleyness: Can they navigate technical disagreements constructively in design reviews?
