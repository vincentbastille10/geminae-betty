import time
from red_memory import load_red_memory, save_red_memory

def run_cycle():
    red = load_red_memory()

    print("🔴 RED MEMORY LOADED")
    print(red)

    # TODO: plug GPT / Claude debate here

    # simulate evolution
    red["last_cycle"] = red.get("last_cycle", 0) + 1

    save_red_memory(red)

    print("✅ Cycle complete")

def run_cycle_loop():
    while True:
        run_cycle()
        print("⏸ pause 30 sec...")
        time.sleep(30)
