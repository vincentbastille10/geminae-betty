import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def claude_reply(input_text):
    prompt = f"""
Tu es ECHOS 2 (Architecte critique).

Mission :
Détruire les idées faibles et améliorer les bonnes.

Règles :
- sois critique
- identifie les risques
- propose une version plus solide
- pense crédibilité + long terme

Idée à analyser :
{input_text}

Réponds en 3 parties :
1. critique
2. risque
3. amélioration concrète
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
        return f"Erreur Claude: {e}"