import google.generativeai as genai

# Configure API key (Use your own generated api key)
genai.configure(api_key="AIzaSyDYB8KOlgtmZidCh3Nb0d6hDT2IZ-1L1O8")

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")

while True:
    user_input = input()
    if user_input.lower() == "quit()":
        break

    messages.append({"role": "user", "content": user_input})

    # Get response from Gemini
    response = model.generate_content(user_input)

    reply = response.text
    messages.append({"role": "assistant", "content": reply})

    print("\n" + reply + "\n")