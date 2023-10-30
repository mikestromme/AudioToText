import os
from dotenv import load_dotenv
import gradio as gr
import whisper


def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    output = result["text"]
    processed_text = "This is an example of processed text."
    return processed_text, output

def download_link(text):
    with open("processed_output.txt", "w") as f:
        f.write(text)
    return "processed_output.txt"

def main():
    audio_input = gr.inputs.Audio(source="upload", type="filepath")
    output_text = gr.outputs.Textbox()
    download_output = gr.outputs.Textbox(label="Download Link")
    
    # iface = gr.Interface(fn=transcribe_audio, inputs=audio_input, 
    #                      outputs=output_text, title="Audio Transcription App",
    #                      description="Upload an audio file and hit the 'Submit' button")
    

    iface = gr.Interface(
    fn=transcribe_audio,
    inputs=audio_input,
    outputs=[output_text, download_output],
    title="Audio Transcription App",
    description="Upload an audio file and hit the 'Submit' button"

)
    
    iface.launch()


if __name__ == '__main__':
    main()
    #output = transcribe_audio("New Recording 6.m4a")
    #print(output)


