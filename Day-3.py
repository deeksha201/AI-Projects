
# AI CHATBOT

# while True:
#     user = input("You: ")
#     if user.lower() == "bye":
#         print("Bot: Goodbye! Have a great day")
#         break
#     print("Bot: You said:", user)



# RULE-BASED CHATBOT

# responses ={
#     "hello":"Hi ! How can I help you?",
#     "goodmorning":"Good morning! How are you?",
#     "hi":"Hello!",
#     "how are you":"I'm doing great!",
#     "what is ai":"AI stands for Artificial Intelligence.",
#     "python":"Python is one of the most popular programming languages.",
#     "bye":"Goodbye!"  
# } 
# while True:
#     user = input("You: ").lower()
#     if user == "bye":
#         print("Bot: responses['bye']")
#         break
#     print("Bot:", responses.get(user, "Sorry, I don't understand that."))



# GEMINI AI CHATBOT

# import google.generativeai as genai
# genai.configure(api_key="enter your api key")
# model = genai.GenerativeModel("gemini-flash-latest")
# print("AI Chatbot")
# print("Type 'exit' to quit.\n")
# while True:
#     user=input("You: ")
#     if user.lower() == "exit":
#         print("Bot: Goodbye! ")
#         break
#     response = model.generate_content(user)
#     print("Bot:", response.text)



# Chatbot with context and memory(History)

# import google.generativeai as genai
# genai.configure(api_key="enter your api key")
# model = genai.GenerativeModel("gemini-flash-latest")
# chat=model.start_chat(history=[])
# print("AI Chatbot")
# print("Type 'exit' to quit.\n")
# while True:
#     user=input("You: ")
#     if user.lower() == "exit":
#         print("Bot: Goodbye! ")
#         break
#     response = chat.send_message(user)
#     print("Bot:", response.text)

# import requests
# url="https://catfact.ninja/fact"
# response=requests.get(url)
# print(response.json())


# import requests
# url="https://official-joke-api.appspot.com/random_joke"
# response=requests.get(url)
# print(response.json())

# import requests
# username=input("Enter your GitHub username: ")
# url=f"https://api.github.com/users/{username}"
# response=requests.get(url)
# print(response.json())


# convert python to json
# import json

# data = {
#     "name": "Deeksha",
#     "age": 20,
#     "course": "AIML"
# }
# json_data = json.dumps(data,indent=4)
# print(json_data)

# convert json to python
# import json

# json_string = '{"name": "Deeksha", "age": 20, "course": "AIML"}'

# python_object = json.loads(json_string)
# print(python_object)
# print(python_object["name"])
# print(python_object["age"])
# print(python_object["course"])
# print(type(python_object))


# import requests
# url="https://api.agify.io?name=Deeksha"
# response=requests.get(url)
# print(response.json())

# print("Name:", response.json()["name"])
# print("Predicted Age:", response.json()["age"])


# POST METHOD
# import requests
# url="https://jsonplaceholder.typicode.com/posts"
# data={
#     "title":"Learning Python",
#     "body":"Python is a versatile programming language.",
#     "userId": 1
# }
# response=requests.post(url,json=data)
# print(response.status_code)
# print(response.json())

# import requests
# url="https://jsonplaceholder.typicode.com/posts"
# Account={
#     "Name":"Deeksha",
#     "age": 20,
#     "course": "AIML",
#     "city": "Madikeri",
# }
# response=requests.post(url,json=Account)
# print(response.status_code)
# print(response.json())


# import requests
# API_KEY="YOUR_NASA_API_KEY"
# url=f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
# response=requests.get(url)
# if response.status_code==200:
#     data=response.json()
#     print("\n==== Astronomy Picture of the Day ====\n")
#     print("Title:", data["title"])
#     print("Date:", data["date"])
#     print("Explanation:", data["explanation"])
#     print("Image URL:", data["url"])
# else:
#     print("Error:", response.status_code, response.text)
#     print(response.text)

# import requests
# ACCESS_KEY="YOUR_UNSPLASH_ACCESS_KEY"
# query=input("Enter a search query Image:")
# url=f"https://api.unsplash.com/search/photos?query={query}&client_id={ACCESS_KEY}"
# params={
#     "query": query,
#     "client_id": ACCESS_KEY,
#     "per_page": 5
# }
# response=requests.get(url, params=params)
# data=response.json()
# print(f"\n=== Search Results for '{query}' ===\n")
# for image in data["results"]:
#             print("Image URL:", image["urls"]["regular"])
#             print("Photographer:", image["user"]["name"])
#             print("Description:", image["description"] or "No description available.")
#             print("-"*40)
