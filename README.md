# 🤖 AI Search & Chat Agent

[![Python](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Repo Size](https://img.shields.io/github/repo-size/ashishsonone26/ai.agent)](https://github.com/ashishsonone26/ai.agent)

A simple & powerful AI assistant combining:
- 🌐 Real-time Google Search (Serper API)
- 🤖 Local AI model (Flan-T5)
- 🧠 Smart agent logic (search + chat)

---

## ✨ Features
- 🔍 **Google Search Integration** using Serper API  
- 🤖 **Local Chatbot** powered by `google/flan-t5-base`  
- 🧠 **Basic conversation memory**  
- 🚀 **Fast & lightweight terminal agent**  
- 🔧 Easy to extend (GPT, Claude, Gemini etc.)

---

## 🛠 Installation

### 1️⃣ Clone the repository
```
git clone https://github.com/ashishsonone26/ai.agent
cd ai.agent
```

### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Add your API key  
Create a file named **.env** in project folder:
```
SERPER_API_KEY=your_api_key_here
```

Get your API key → https://serper.dev/

---

## ▶️ How to Run
```
python main.py
```

### 💬 Example Usage
```
You: hello
AI: hi! how can I assist you today?

You: search: india prime minister
AI: Narendra Modi is the current prime minister of India...
```

---

## 📁 Project Structure
```
ai.agent/
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE (optional)
```

---

## 🚧 Future Improvements
- Add Streamlit web UI  
- Add voice commands (speech-to-text)  
- Add YouTube video summarizer  
- Add long-term memory using FAISS  
- Add multiple tools: calculator, weather, system info  

---

## 👤 Author
**Ashish Sonone**  
🔗 GitHub: https://github.com/ashishsonone26  



