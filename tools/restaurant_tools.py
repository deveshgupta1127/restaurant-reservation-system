from utils.data_loader import load_json

RESTAURANT_PATH = "data/restaurants.json"

def search_restaurants(location, cuisine=None):
    restaurants = load_json(RESTAURANT_PATH)
    results = []

    for r in restaurants:
        if r["location"].lower() == location.lower():
            if cuisine:
                if cuisine.lower() in [c.lower() for c in r["cuisine"]]:
                    results.append(r)
            else:
                results.append(r)

    return results[:5]

def recommend_restaurants(party_size):
    restaurants = load_json(RESTAURANT_PATH)
    suitable = [r for r in restaurants if r["capacity"] >= party_size]
    return sorted(suitable, key=lambda x: x["rating"], reverse=True)[:3]
