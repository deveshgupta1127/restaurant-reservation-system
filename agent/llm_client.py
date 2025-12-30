from groq import Groq
from config.settings import GROQ_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS

client = Groq(api_key=GROQ_API_KEY)

def call_llm(messages, tools):
    return client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools,
        tool_choice="auto",
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )
