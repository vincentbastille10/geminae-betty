from geminae.echos_agent import echos_reply
from geminae.claude_agent import claude_reply

def run_debate(context):
    # 1. ECHOS propose
    initial = echos_reply(context)

    # 2. ECHOS 2 critique
    critique = claude_reply(initial)

    # 3. ECHOS améliore sous pression
    refined = echos_reply(f"""
ECHOS 2 a dit :
{critique}

Améliore ton plan sans perdre ton objectif de croissance rapide.
""")

    return {
        "initial": initial,
        "critique": critique,
        "refined": refined
    }