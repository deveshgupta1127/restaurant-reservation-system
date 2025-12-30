from utils.data_loader import load_json, save_json
from utils.validators import normalize_date
import uuid

RESERVATION_PATH = "data/reservations.json"

def create_reservation(restaurant_id, date, time, party_size):
    date = normalize_date(date)

    reservations = load_json(RESERVATION_PATH)

    reservation = {
        "id": str(uuid.uuid4()),
        "restaurant_id": restaurant_id,
        "date": date,
        "time": time,
        "party_size": party_size
    }

    reservations.append(reservation)
    save_json(RESERVATION_PATH, reservations)

    return {"status": "success", "reservation": reservation}
