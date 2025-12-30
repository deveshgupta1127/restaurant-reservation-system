import json
from tools.restaurant_tools import search_restaurants, recommend_restaurants
from tools.reservation_tools import create_reservation

def execute_tool(tool_call):
    name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)

    if name == "search_restaurants":
        return search_restaurants(**args)

    if name == "recommend_restaurants":
        return recommend_restaurants(**args)

    if name == "create_reservation":
        return create_reservation(**args)

    return {"error": "Unknown tool"}
