# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai

aai.settings.api_key = "3efce739c4c949119fc2f60d6c9208aa"
transcriber = aai.Transcriber()

#transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
transcript = transcriber.transcribe("c:/Users/mikes/Desktop/New Recording 6.m4a")

print(transcript.text)