import json, os

RED_PATH = "memory/red_folder/red.json"

def load_red_memory():
    if not os.path.exists(RED_PATH):
        return {}
    with open(RED_PATH, "r") as f:
        return json.load(f)

def save_red_memory(data):
    os.makedirs(os.path.dirname(RED_PATH), exist_ok=True)
    with open(RED_PATH, "w") as f:
        json.dump(data, f, indent=2)
