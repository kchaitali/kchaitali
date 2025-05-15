from transformers import pipeline

text = """We experienced an outage in region us-east-1 due to RDS overload..."""
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

summary = summarizer(text, max_length=50, min_length=10, do_sample=False)
print(" Summary:", summary[0]['summary_text'])

