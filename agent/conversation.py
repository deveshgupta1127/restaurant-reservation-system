from agent.llm_client import call_llm
from agent.tool_router import execute_tool
from config.prompts import SYSTEM_PROMPT
import json

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_restaurants",
            "description": "Search restaurants by location and cuisine",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "cuisine": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "recommend_restaurants",
            "description": "Recommend restaurants based on party size",
            "parameters": {
                "type": "object",
                "properties": {
                    "party_size": {"type": "integer"}
                },
                "required": ["party_size"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_reservation",
            "description": "Create a reservation",
            "parameters": {
                "type": "object",
                "properties": {
                    "restaurant_id": {"type": "string"},
                    "date": {"type": "string"},
                    "time": {"type": "string"},
                    "party_size": {"type": "integer"}
                },
                "required": ["restaurant_id", "date", "time", "party_size"]
            }
        }
    }
]

def handle_conversation(messages):
    response = call_llm(messages, TOOLS)
    msg = response.choices[0].message

    # TOOL CALL PATH
    if msg.tool_calls:
        tool_call = msg.tool_calls[0]
        tool_result = execute_tool(tool_call)

        messages.append({
            "role": "assistant",
            "content": None,
            "tool_calls": msg.tool_calls
        })

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(tool_result)
        })

        return handle_conversation(messages)

    # NORMAL ASSISTANT MESSAGE
    assistant_message = {
        "role": "assistant",
        "content": msg.content
    }

    return msg.content
