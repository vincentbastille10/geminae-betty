from geminae.friction_engine import run_debate
from geminae.final_synthesizer import synthesize
from red_memory import load_red_memory, save_red_memory
import time

def run_cycle():
    red = load_red_memory()

    debate = run_debate(red)
    decision = synthesize(debate)

    red["last_decision"] = decision

    save_red_memory(red)

    print("\n🧠 DECISION:\n")
    print(decision)

def run_cycle_loop():
    while True:
        run_cycle()
        print("\n⏸ pause 30 sec...\n")
        time.sleep(30)