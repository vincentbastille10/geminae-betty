import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def synthesize(debate):
    prompt = f"""
Tu es un CEO stratégique.

Analyse ce débat :

{debate}

Donne :
1. la meilleure décision business
2. une action immédiate à lancer
3. ce qu’il ne faut SURTOUT PAS faire
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
        return f"Erreur synthèse: {e}"