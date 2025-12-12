import json, os
from datetime import datetime

task_files =  "task.json"

def load_task():
    if not os.path.exists(task_files):
        return []
    with open (task_files, "r") as f:
        return json.load(f)
    