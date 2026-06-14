import json
from pathlib import Path

FILE = Path("tasks.json")

def load_tasks():
    if FILE.exists():
        return json.loads(FILE.read_text())
    return []

def save_tasks(tasks):
    FILE.write_text(json.dumps(tasks, indent=2))
