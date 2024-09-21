#Get the list of models available in open AI
import os
import openai

# This the file got created a a global environment file , where you have to set the API key and org key for your account
import openaienv
openai.organization = openaienv.GLOBAL_ORG_KEY
openai.api_key = openaienv.GLOBAL_API_KEY
model_lst = openai.Model.list()
for i in model_lst['data']:
    print(i['id'])

