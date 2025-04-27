# Random Realms: AI-Generated Puzzle Game 🧩

Random Realms is a unique puzzle game that generates its story, puzzles, graphics, and audio using AI every time you play.

**Learn about LLMs by playing and contributing to this project.**

## Setup:

1.  `git clone <repository_url>`
2.  `cd Random-Realms`
3.  `python -m venv venv && source venv/bin/activate` (*macOS/Linux*) or `venv\Scripts\activate` (*Windows*)
4.  `pip install -r requirements.txt`
5.  Get API keys from [Replicate](https://replicate.com/), [OpenRouter](https://openrouter.ai/), and [ElevenLabs](https://elevenlabs.io/).
6.  Set environment variables:
    ```bash
    export OPENROUTER_API_KEY=YOUR_KEY
    export REPLICATE_API_TOKEN=YOUR_KEY
    export ELEVENLABS_API_KEY=YOUR_KEY
    ```
7.  Run: `python main.py` (Level generation takes ~1 minute).

## Contribute:

Check [invalid URL removed] for issues and feel free to submit improvements.

## Nightmare Mode:

Toggle `NIGHTMARE_MODE` in `prompts.py` for a scarier experience.
