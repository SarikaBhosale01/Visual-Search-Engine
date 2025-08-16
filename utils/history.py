import json
import datetime

def save_to_history(filename, label):
    history = []
    try:
        with open("history.json", "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        pass
    history.insert(0, {
        "image": filename,
        "label": label,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    with open("history.json", "w") as f:
        json.dump(history[:10], f)  # Keep only last 10
