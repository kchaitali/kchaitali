from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

tools = [
    Tool(name="ExplainLogs", func=lambda q: f"Investigating: {q}", description="Explains logs or errors")
]

agent = initialize_agent(tools, OpenAI(temperature=0), agent="zero-shot-react-description")

response = agent.run("Explain 'CrashLoopBackOff' in Kubernetes")
print("Agent:", response)

