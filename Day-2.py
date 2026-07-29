from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

prompt = """
Classify the sentiment of the following sentence as
POSITIVE, NEGATIVE, or NEUTRAL.

Sentence:
The delivery was late but the food was amazing.

Answer:
"""

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=10)
result_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(result_text)

from transformers import pipeline
generator=pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct"  )
message=[
    {
        "role": "user",
        "content": """Classify the sentiment.
        Examples:
        sentence: I love coorg!
        sentiment: POSITIVE
        
    sentence:I hate flood in coorg!
    sentiment: NEGATIVE
    
    sentence: The cit is okay.
    sentiment: NEUTRAL
    
    Now classify :
    Sentence:The pork in coorg is fantastic!
    Sentiment:
    """
    }
]
result=generator(message, max_new_tokens=20)
print(result[0]["generated_text"][-1]["content"])

