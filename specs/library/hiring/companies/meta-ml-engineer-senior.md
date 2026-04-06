---
kind: hiring
role: Senior ML Engineer
team: AI / GenAI
level: L5
version: 1
---

# What We're Looking For

We move fast and ship models to 3 billion people. If you've only trained models on clean datasets with obvious metrics, this role isn't for you. We need someone who's debugged training runs at 2am, shipped a model that broke in production, and iterated their way to something that actually moves metrics.

Bootcamp means you'll pick your team after 6 weeks, but I'm betting on GenAI being the highest-impact area at Meta right now. Llama didn't happen by accident — we have infrastructure, data, and talent that most places dream about. But infrastructure without taste is just expensive compute.

The best candidates understand that ML at our scale isn't just bigger — it's qualitatively different. Your model choices affect our infrastructure costs by millions. Your evaluation framework affects product decisions for billions of users. Your code review comments teach the next generation of ML engineers what good looks like.

## Must-Haves

- Trained large language models from scratch (not just fine-tuning someone else's checkpoint)
- Shipped an ML system that failed in production and can walk through the debugging process
- Written CUDA kernels or optimized training loops (PyTorch internals, gradient accumulation, mixed precision)
- Experience with distributed training at scale (multi-node, data/model parallelism trade-offs)

## Strong Signals

- Open source contributions to PyTorch, transformers, or similar frameworks
- Has opinions about evaluation that go beyond perplexity and BLEU scores
- Built internal tools or frameworks that other ML engineers actually used
- Hackathon projects that shipped (shows you can move from idea to production fast)

## Anti-Patterns

- "ML Engineer" experience that was really just API calls to OpenAI
- Can't explain why their model architecture choices matter for their specific problem
- Treats model serving as someone else's problem
- Never questioned whether their evaluation metrics actually correlate with user value
- Obsesses over perfect code instead of iterating toward impact

## Interview Focus

- System design: How would you build Llama training infrastructure? What are the bottlenecks?
- Model debugging: Walk through a time your model performed worse than expected. How did you isolate the issue?
- Technical taste: Given our compute budget, how would you allocate resources between model size, data quality, and training time?
- Impact measurement: How do you know if your GenAI feature is actually helping users vs. just being technically impressive?
