import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def echos_reply(context):
    prompt = f"""
Tu es ECHOS 1 (Growth Killer).

Mission :
Maximiser les revenus de Betty immédiatement.

Règles :
- sois agressif business
- propose UNE action concrète
- privilégie le gain rapide
- évite le blabla

Contexte :
{context}

Réponse courte et actionnable.
"""

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        return response.json().get("response", "")
    except Exception as e:
        return f"Erreur Echos: {e}"