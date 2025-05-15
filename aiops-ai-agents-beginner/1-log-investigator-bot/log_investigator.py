from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

log_snippet = """
ERROR [2024-05-13 12:01:01] ConnectionTimeout: Failed to reach database after 30s retry.
"""

prompt = ChatPromptTemplate.from_template(
    "Explain the cause and next steps for this log error:\n{log}"
)

llm = ChatOpenAI(model_name="gpt-3.5-turbo")
response = llm.predict(prompt.format(log=log_snippet))

print("Explanation:", response)
