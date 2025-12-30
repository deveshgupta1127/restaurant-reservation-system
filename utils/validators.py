from datetime import datetime, timedelta

def check_capacity(restaurant, party_size):
    return restaurant["capacity"] >= party_size

def is_valid_time(time_str):
    return True  # keep simple for demo

def normalize_date(date_str):
    date_str = date_str.lower().strip()

    if date_str == "today":
        return datetime.today().strftime("%Y-%m-%d")

    if date_str == "tomorrow":
        return (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    # assume already valid
    return date_str
