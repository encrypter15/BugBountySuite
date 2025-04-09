# ai_analyzer.py—hooking up to the big AI guns!
import logging
import requests
import json
import os

# Load AI config from a JSON file—user’s gotta set this up
CONFIG_FILE = "data/ai_config.json"

def load_ai_config():
    # Grab those sweet API keys—don’t fuck it up!
    if not os.path.exists(CONFIG_FILE):
        default_config = {
            "Gemini": {"api_key": "", "endpoint": "https://api.gemini.com/v1/analyze"},
            "xAI": {"api_key": "", "endpoint": "https://api.x.ai/v1/completions"},
            "ChatGPT": {"api_key": "", "endpoint": "https://api.openai.com/v1/chat/completions"}
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(default_config, f, indent=4)
        logging.warning(f"Created default AI config at {CONFIG_FILE}—fill in your keys, dumbass!")
        return default_config
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def analyze_with_gemini(title, poc, severity):
    # Gemini AI—hypothetical endpoint, adjust when real docs drop
    config = load_ai_config()["Gemini"]
    if not config["api_key"]:
        return 0.0
    payload = {
        "text": f"Vulnerability: {title}\nPoC: {poc}\nSeverity: {severity}",
        "task": "assess_vulnerability"
    }
    headers = {"Authorization": f"Bearer {config['api_key']}"}
    try:
        resp = requests.post(config["endpoint"], json=payload, headers=headers, timeout=10)
        resp.raise_for_status()
        score = resp.json().get("score", 0.0)  # Assume 0-10 scale
        logging.info(f"Gemini scored {title}: {score}")
        return min(score / 10, 1.0)  # Normalize to 0-1
    except Exception as e:
        logging.error(f"Gemini failed: {e}")
        return 0.0

def analyze_with_xai(title, poc, severity):
    # xAI—hypothetical, based on typical API patterns
    config = load_ai_config()["xAI"]
    if not config["api_key"]:
        return 0.0
    payload = {
        "prompt": f"Assess this vuln: Title: {title}, PoC: {poc}, Severity: {severity}. Return a score 0-10.",
        "max_tokens": 50
    }
    headers = {"Authorization": f"Bearer {config['api_key']}"}
    try:
        resp = requests.post(config["endpoint"], json=payload, headers=headers, timeout=10)
        resp.raise_for_status()
        score = float(resp.json()["choices"][0]["text"].strip())  # Assume it spits a number
        logging.info(f"xAI scored {title}: {score}")
        return min(score / 10, 1.0)
    except Exception as e:
        logging.error(f"xAI failed: {e}")
        return 0.0

def analyze_with_chatgpt(title, poc, severity):
    # ChatGPT—real OpenAI API, baby
    config = load_ai_config()["ChatGPT"]
    if not config["api_key"]:
        return 0.0
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You’re a vuln assessor. Score 0-10 based on exploitability."},
            {"role": "user", "content": f"Title: {title}\nPoC: {poc}\nSeverity: {severity}"}
        ],
        "max_tokens": 10
    }
    headers = {"Authorization": f"Bearer {config['api_key']}", "Content-Type": "application/json"}
    try:
        resp = requests.post(config["endpoint"], json=payload, headers=headers, timeout=10)
        resp.raise_for_status()
        score = float(resp.json()["choices"][0]["message"]["content"].strip())
        logging.info(f"ChatGPT scored {title}: {score}")
        return min(score / 10, 1.0)
    except Exception as e:
        logging.error(f"ChatGPT failed: {e}")
        return 0.0

def analyze_vulnerability(title, poc, severity, ai_providers):
    # Orchestrate the AI party—stack ‘em or solo!
    if not ai_providers:
        return 0.0
    scores = []
    if "Gemini" in ai_providers:
        scores.append(analyze_with_gemini(title, poc, severity))
    if "xAI" in ai_providers:
        scores.append(analyze_with_xai(title, poc, severity))
    if "ChatGPT" in ai_providers:
        scores.append(analyze_with_chatgpt(title, poc, severity))
    return sum(scores) / len(scores) if scores else 0.0  # Average the scores, bitches!
