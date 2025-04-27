import os 
import json
import base64
import asyncio

from flask import Flask, render_template, jsonify, request

from prompts import INITIAL_PROMPT
from openai import OpenAI
import replicate
from elevenlabs.client import ElevenLabs


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

eleven_client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)


app = Flask(__name__)


@app.route("/")
def home_view():
    return render_template("home.html")

@app.route("/generate-story", methods=["POST"])
def generate_story_view():
    request_data = request.get_json()
    action = request_data.get("action", None)
    history = request_data.get("conversation_history")

    if not action:
        prompt = INITIAL_PROMPT
    else:
        prompt = f"{INITIAL_PROMPT}\n\n{history}\n\n{action}"

    completion = client.chat.completions.create(
    model="openai/gpt-4o",
    messages=[
        {
        "role": "user",
        "content": prompt 
        }
    ]
    )
    content = completion.choices[0].message.content
    cleaned_content = content.replace("json", "").replace("```", "")
    content_json = json.loads(cleaned_content)
    description = content_json["description"]
    actions = content_json["actions"]
    music_description = content_json["music_description"]

    async def generate_image():
        input_data = {"aspect_ratio": "16:9", "prompt": description}
        output = replicate.run("recraft-ai/recraft-v3", input=input_data)
        image_data = output.read()
        image_base64 = base64.b64encode(image_data).decode("utf-8")
        return image_base64

    async def generate_music():
        music_input = {"prompt": music_description, "duration": 30}

        music_output = replicate.run(
            "ardianfe/music-gen-fn-200e:96af46316252ddea4c6614e31861876183b59dce84bad765f38424e87919dd85",
            input=music_input,
        )
        audio_bytes = music_output.read()
        audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
        return audio_base64

    async def generate_voice():
        voice = eleven_client.generate(
            text=description,
            voice="JBFqnCBsd6RMkjVDRZzb",
            model="eleven_multilingual_v2",
        )
        voice_bytes = b"".join(voice)
        return base64.b64encode(voice_bytes).decode("utf-8")


    async def main():
        image_base64, music_base64, voice_base64 = await asyncio.gather(
            generate_image(), generate_music(), generate_voice()
        )
        return image_base64, music_base64, voice_base64

    image_base64, music_base64, voice_base64  = asyncio.run(main())




    response_data = {
        "description": description,
        "actions": actions,
        "image": image_base64,
        "music": music_base64,
        "voice": voice_base64
    }
    
    return jsonify(response_data)




if __name__ == "__main__":
    app.run(debug=True)
