
from google import genai

client = genai.Client(
    api_key="Enter-Your-API-Key-Here"
)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)