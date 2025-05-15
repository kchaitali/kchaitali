import openai

openai.api_key = "your-api-key"

alert = "High CPU usage on node ip-10-0-0-5"
prompt = f"""Given the alert: '{alert}', suggest a YAML-formatted remediation plan."""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

print(" Remediation Plan:\n", response['choices'][0]['message']['content'])

