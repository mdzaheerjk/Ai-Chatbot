# 🤖 Gemini AI Chatbot CLI (Python)

A command-line chatbot powered by **Google Gemini API**. It allows you to chat with Google's powerful generative models like `gemini-2.0-flash-001`. This tool supports retry handling, model listing, and clean output directly from your terminal.

---

## 🚀 Features

| Feature                         | Description                                                  |
|-------------------------------|--------------------------------------------------------------|
| 🔐 Secure Gemini API access    | Easily plug in your API key                                  |
| 🧠 Multiple model support      | Lists all available Gemini models                            |
| 💬 Interactive CLI Chat        | Real-time chatbot via terminal input/output                  |
| 🛡️ Retry mechanism             | Built-in retry with exponential backoff for rate limits      |
| 🧪 Error handling              | Graceful handling of exceptions (invalid key, connectivity)  |

---

## 🧰 Requirements

- Python 3.7+
- `google-generativeai` library

Install with:

```bash
pip install google-generativeai
