# Random Realms: AI-Generated Puzzle Game 🧩

Random Realms is a unique puzzle game that generates its story, puzzles, graphics, and audio using AI every time you play.


![Screenshot from 2025-04-27 10-59-57](https://github.com/user-attachments/assets/bfec08b9-6b5f-47b2-9b1f-fdaf488d6b6d)

**Learn about LLMs by playing and contributing to this project.**

## Setup:

1.  `git clone https://github.com/GGyll/random_realms`
2.  `cd Random-Realms`
3.  `python -m venv venv && source venv/bin/activate` (*macOS/Linux*) or `venv\Scripts\activate` (*Windows*)
4.  `pip install -r requirements.txt`
5.  Get API keys from [Replicate](https://replicate.com/), [OpenRouter](https://openrouter.ai/), and [ElevenLabs](https://try.elevenlabs.io/meljryj15ura).
6.  Add these environment variables to the bottom .venv/bin/activate file:
    ```bash
    export OPENROUTER_API_KEY=YOUR_KEY
    export REPLICATE_API_TOKEN=YOUR_KEY
    export ELEVENLABS_API_KEY=YOUR_KEY
    ```
7.  Run: `python main.py` (Level generation takes ~1 minute, so be patient).

## Contribute:

Feel free to submit any improvements!

## Nightmare Mode:

Toggle `NIGHTMARE_MODE` in `prompts.py` for a scarier experience.
