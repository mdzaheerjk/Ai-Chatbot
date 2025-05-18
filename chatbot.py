import os
import time
import google.generativeai as genai

# 🔐 Configure Gemini with API key
api_key = "AIzaSyDv_iGRWko9CZ8DO0NMWJNyo0JLusERoZo"
genai.configure(api_key=api_key)

# List available models with detailed information
print("\n🔍 Available Models:")
print("-------------------")
try:
    models = genai.list_models()
    for m in models:
        print(f"\nModel: {m.name}")
        print(f"Display Name: {m.display_name}")
        print(f"Description: {m.description}")
        print("Supported Methods:")
        for method in m.supported_generation_methods:
            print(f"  - {method}")
        print("-------------------")
except Exception as e:
    print(f"Error listing models: {e}")

# ✅ Use Gemini model
try:
    model = genai.GenerativeModel('gemini-2.0-flash-001')
    chat = model.start_chat(history=[])
    print("\n🤖 Gemini Chatbot initialized successfully!")
except Exception as e:
    print(f"⚠️ Failed to initialize model: {e}")
    print("Please check your API key and internet connection.")
    exit()

print("\n🤖 Gemini Chatbot — type 'exit' to stop")

def send_message_with_retry(message, max_retries=3, delay=2):
    for attempt in range(max_retries):
        try:
            response = chat.send_message(message)
            return response.text
        except Exception as e:
            if "429" in str(e):  # Rate limit error
                if attempt < max_retries - 1:
                    print(f"Rate limit hit. Waiting {delay} seconds before retry...")
                    time.sleep(delay)
                    delay *= 2  # Exponential backoff
                else:
                    return "Sorry, I'm currently experiencing high traffic. Please try again in a few minutes."
            else:
                return f"Error: {str(e)}"
    return "Sorry, I'm unable to process your request at the moment."

while True:
    try:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye! 👋")
            break

        response = send_message_with_retry(user_input)
        print("Bot:", response)
    except KeyboardInterrupt:
        print("\nBot: Goodbye! 👋")
        break
    except Exception as e:
        print(f"Unexpected error: {e}")
        print("Please try again or type 'exit' to quit.")
