import os
from autogen import ConversableAgent 

config_list =[
    {
        "model":"",
        "api_key": os.getenv("OPEN_AI_KEY"),
        "base_url":"",
        "api_version":"",
        "api_type":"openai"
    }
]

llm_config= {
    "seed": 42,
    "config_list":config_list,
    "temperature":0.5
}

user1 = ConversableAgent(
    "Rakesh",
    system_message="Your name is Rakesh and you are male",
    llm_config=llm_config,
    human_input_mode="NEVER",
    )

user2 = ConversableAgent(
    "Shilpi",
    system_message="Your name is Shilpi and you are female",
    llm_config=llm_config,
    human_input_mode="NEVER",
    )

result = user2.initiate_chat(user1,message="Rakesh, tell me a joke.",max_turns=3)