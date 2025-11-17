import os
import requests
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# ======================================================
# 🔍 GOOGLE SEARCH (Serper API) — with better error handling
# ======================================================
def google_search(query):
    url = "https://google.serper.dev/search"
    payload = {"q": query}
    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        return f"❌ Search Error: {e}"

    # Answer box priority
    if data.get("answerBox"):
        return data["answerBox"].get("answer") or data["answerBox"].get("snippet")

    # Organic results
    organic = data.get("organic", [])
    if organic:
        return organic[0].get("snippet")

    return "❌ No results found."


# ======================================================
# 🤖 AI MODEL (Better & faster than Blenderbot)
# ======================================================

MODEL_NAME = "google/flan-t5-base"   # More accurate & free

print("⏳ Loading AI model... please wait...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Simple conversation memory
conversation_history = []


def chat_response(text):
    conversation_history.append(f"User: {text}")

    # Combine last 5 messages only (memory)
    context = "\n".join(conversation_history[-5:])  
    prompt = f"{context}\nAI:"

    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**inputs, max_length=150)
    reply = tokenizer.decode(output[0], skip_special_tokens=True)

    conversation_history.append(f"AI: {reply}")
    return reply


# ======================================================
# 🚀 MAIN AGENT LOGIC
# ======================================================
def main():
    print("🤖 AI + 🌐 Search Agent Ready!")
    print("Commands:")
    print("➡ search: <your question>")
    print("➡ chat normally for AI")
    print("➡ exit to quit\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break

        # Auto-detect search intent
        if user_input.lower().startswith("search:") or "search" in user_input.lower():
            query = user_input.replace("search:", "").replace("search", "").strip()
            print("\n🌐 Searching Google...\n")
            result = google_search(query)
            print("📌 Result:", result, "\n")

        else:
            reply = chat_response(user_input)
            print("\nAI:", sreply, "\n")


if __name__ == "__main__":
    main()









