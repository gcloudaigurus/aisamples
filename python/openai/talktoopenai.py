# Example of an OpenAI ChatCompletion request with stream=False and using GPT models
import os
import openai
# This the file got created a a global environment file , where you have to set the API key and org key for your account
import openaienv

openai.organization = openaienv.GLOBAL_ORG_KEY
openai.api_key = openaienv.GLOBAL_API_KEY
# a ChatCompletion request for calcualting the first 100 prime numbers sum
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'user', 'content': "calculate the sum of first 100 prime numbers"}
    ],
    temperature=0,
    stream=False  # this time, we set stream=False
)
message_json = response['choices']
for i in message_json:
    print(i['message']['content'])
