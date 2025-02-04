import google.generativeai as genai

# Configure API key (Replace with your own key)
genai.configure(api_key="AIzaSyDYB8KOlgtmZidCh3Nb0d6hDT2IZ-1L1O8")

# Initialize Gemini model
model = genai.GenerativeModel("gemini-pro")

# Generate response
response = model.generate_content("Give me 3 ideas for apps I could build with Google Gemini API")

# Print the response
print(response.text)
