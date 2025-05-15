# 🤖 Beginner-Friendly AIOps Projects Using AI Agents

Welcome! This repo contains 4 beginner-friendly AIOps projects powered by AI agents. These projects are perfect for DevOps/SRE engineers who want to dip their toes into AIOps and generative AI.

Each project is:
- Lightweight and easy to understand
- Uses Python + Open Source Libraries
- Built to solve common Ops problems with AI help

---

## 🔧 Projects

### 1. Log Investigator Bot
Use GPT to explain and diagnose log errors.

🧠 Goal:
Ask an agent: "What’s wrong with this log?" and it explains.

🧰 Tools:
LangChain

OpenAI API

Python (or Streamlit)

📂 `1-log-investigator-bot/log_investigator.py`

---

### 2. Incident Summary Agent
Summarize incident reports or tickets using HuggingFace summarization models.

📂 `2-incident-summary-agent/incident_summary.py`

🧠 Goal:
Takes a long Jira ticket or alert email and gives a concise summary.

🧰 Tools:
HuggingFace Transformers

Flask or FastAPI

BART / T5 model
---

### 3. ChatOps Assistant
Chat with an LLM-powered DevOps assistant that can explain terms, errors, or guide you.

📂 `3-chatops-assistant/chatops_agent.py`

🧠 Goal:
Chat with your own DevOps LLM Agent to ask:

"What does this Kubernetes error mean?"

🧰 Tools:
LangChain

Slack Bot / Telegram Bot

OpenAI

---

### 4. Auto-Remediation Planner
Give an alert as input, and get back a GPT-generated YAML remediation plan.

📂 `4-auto-remediation-planner/remediation_planner.py`

🧠 Goal:
Feed an alert, get a GPT-generated remediation plan.

🧰 Tools:
OpenAI GPT-4

YAML Playbook Generator

Shell scripts (optional)

---

## 📦 Setup

1. Clone the repo  
```bash
git clone https://github.com/your-username/aiops-ai-agents-beginner.git
cd aiops-ai-agents-beginner

2. Install Dependencies
```bash
pip install -r requirements.txt

3. Add your API keys (OpenAI or HuggingFace)

4. Run any script
```bash
python 1-log-investigator-bot/log_investigator.py

Feedback / Contributions
Open to feedback, ideas, and PRs! Ping me on LinkedIn if you build something cool with this. 🚀


