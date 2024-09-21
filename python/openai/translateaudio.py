# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
#Get the list of models available in open AI
import os
import openai

# This the file got created a a global environment file , where you have to set the API key and org key for your account
import openaienv
openai.organization = openaienv.GLOBAL_ORG_KEY
openai.api_key = openaienv.GLOBAL_API_KEY

#Please donwload and place the file to correct directory from 
# https://content.libsyn.com/p/3/5/0/35042c3ec82b36e8/Your_First_Lesson.mp3?c_id=1940717&cs_id=1940717&response-content-type=audio%2Fmpeg&Expires=1689349211&Signature=CVTrlMYOrXMgvvvoyZvF9OvyH9zQm802DenasCF8YnUKSIui6ohj9hx-3bUCGIWABIZwAgAFbWUkGchSD0tquTvEgxDCHt~LRDrfy-WyTqJSQLx-2Yi56Pi76O30aee0ujIphKu3DIkefUo-HEzr9ZIXCid8Uio7TTthbP2J~Vfljs5kNIqNCJDPuFqQDI1NqeVxZvjXF5m7QetbSobSus4d4SmwbqtgHAiIa-6vQ~Lx7JS6YL1~rI9l8MpxDxWDj2sQuCQheG-poQIwtgPDbjgI5OxvVlGe36tWtKBk5Vtyb~HupySzQx6aGdABoJL~~pflNi8rPAUYtbto0YsbwQ__&Key-Pair-Id=K1YS7LZGUP96OI
#audio_file= open("Your_First_Lesson.mp3", "rb")
audio_file= open("C:\\PRODDEV\\projects\\cloudaigurus\\content\\sampleaudios\\recording0.wav", "rb")

transcript = openai.Audio.translate("whisper-1", audio_file)
print(transcript)