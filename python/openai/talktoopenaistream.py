# Example of an OpenAI ChatCompletion request with stream=True and using GPT models
# streaming is faster and better for many applications
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
    stream=True  # this time, we set stream=True
)

# create variables to collect the stream of chunks
collected_chunks = []
collected_messages = []
# iterate through the stream of events
for chunk in response:
    collected_chunks.append(chunk)  # save the event response
    chunk_message = chunk['choices'][0]['delta']  # extract the message
    collected_messages.append(chunk_message)  # save the message

# print the time delay and text received
full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
print(f"Full conversation received: {full_reply_content}")