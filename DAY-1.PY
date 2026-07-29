# user={
#     "name":"Deeksha",
#     "city" : "Madikeri",
#     "order":"Pork"

# }
# print(f"Hello{user['name']}!")
# print(f"Delivering {user['order']} to {user['city']}.")


# user={
#     "name":"Deeksha",
#     "followers": 1000,
#     "likes": 500,   
# }
# print(f"{user['name']} has {user['followers']} followers.")
# print(f"{user['name']} has {user['likes']} likes.")


# from transformers import pipeline
# classifier=pipeline("sentiment-analysis")
# result = classifier("I love eating idly in coorg")
# print(result)

# from transformers import pipeline
# classifier=pipeline("sentiment-analysis")
# result = classifier(" Coorg has a bad weather")
# print(result)

# from transformers import pipeline
# generator=pipeline("text-generation",model="gpt2")
# output=generator("Artificial Intelligence will",max_length=40)
# print(output[0]['generated_text'])

# from transformers import pipeline
# generator=pipeline("text-generation",model="gpt2")
# output=generator("Once open a time in madikeri,",max_length=40)
# print(output[0]['generated_text'])

# from transformers import pipeline
# generator=pipeline("text-generation",model="gpt2")
# output=generator("Give me a lame joke",max_length=40)
# print(output[0]['generated_text'])



# import requests
# import os

# API_KEY=os.getenv("HF_API_KEY")
# response=requests.post("https://api-inference.huggingface.co/models/gpt2", headers={"Authorization": f"Bearer {API_KEY}"}, json={"inputs": "Python is great because"})
# print(response.json())
