#This sample will create a audio file as you speak and translate the audio to text and pass that to open AI GPT model for answering 
import os
import openai

# This the file got created a a global environment file , where you have to set the API key and org key for your account
import openaienv
openai.organization = openaienv.GLOBAL_ORG_KEY
openai.api_key = openaienv.GLOBAL_API_KEY
system_prompt = "You are a helpful assistant for the company cloudaigurus. Your task is translate the audio."

# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
 
# Sampling frequency
freq = 44100

# Sample audio file location, please change this location as per your system
sample_audio_file_location = "C:\\PRODDEV\\projects\\cloudaigurus\\content\\sampleaudios\\"
# Recording duration
duration = 5
 
# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=2)
 
# Record audio for the given number of seconds
sd.wait()
 
# This will convert the NumPy array to an audio
# file with the given sampling frequency
write(sample_audio_file_location + "recording0.wav", freq, recording)
 
# Convert the NumPy array to audio file
wv.write(sample_audio_file_location + "recording1.wav", recording, freq, sampwidth=2)

def generate_answer_transcript(temperature, system_prompt, audio_file):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": ""
            },
            {
                "role": "user",
                "content": str(openai.Audio.translate("whisper-1", audio_file))
            }
        ]
    )
    return response['choices'][0]['message']['content']
sample_audio_file= open(sample_audio_file_location + "recording0.wav", "rb")

response_text = generate_answer_transcript(0, system_prompt, sample_audio_file)
print("Response is :" + response_text)