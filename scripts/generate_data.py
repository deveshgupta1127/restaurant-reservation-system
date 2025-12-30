import json
import random
import uuid

locations = ["Madhapur", "Gachibowli", "Banjara Hills"]
cuisines = ["Italian", "Indian", "Chinese", "Mexican"]

restaurants = []

for i in range(60):
    restaurants.append({
        "id": str(uuid.uuid4()),
        "name": f"GoodFoods {i}",
        "location": random.choice(locations),
        "cuisine": random.sample(cuisines, 2),
        "capacity": random.randint(20, 100),
        "rating": round(random.uniform(3.5, 4.8), 1),
        "price_range": random.choice(["₹₹", "₹₹₹"])
    })

with open("data/restaurants.json", "w") as f:
    json.dump(restaurants, f, indent=2)
