from fastapi import FastAPI
import os

app = FastAPI()

# Need to store the state of counter somewhere locally. Can use db for this local txt file is used
COUNTER_FILE = "counter_state.txt"

# This is to get the current counter value
def get_counter():
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "w") as f:
            f.write("0")
        return 0
    with open(COUNTER_FILE, "r") as f:
        return int(f.read().strip())

# This is to set the counter value
def set_counter(value):
    with open(COUNTER_FILE, "w") as f:
        f.write(str(value))

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/counter")
def counter():
    count = get_counter() + 1
    set_counter(count)
    return f"Counter value: {count}"
