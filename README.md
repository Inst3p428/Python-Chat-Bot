# 🤖 CryptoBuddy – Rule-Based Crypto Investment Chatbot

CryptoBuddy is a simple rule-based chatbot built with Python that analyzes predefined cryptocurrency data to provide friendly investment advice based on **profitability** and **sustainability**.

---

## 💡 Features

- ✅ Conversational chatbot interface
- 📈 Recommends profitable cryptocurrencies (based on price trends & market cap)
- 🌱 Suggests eco-friendly, sustainable coins (based on energy use & sustainability score)
- 🧠 Uses simple `if-else` logic (no ML required)
- 🛠️ Easily extendable with real-time APIs or NLP tools

---

## 🛠️ Technologies Used

- **Python 3.x**
- Simple `if-else` logic (no external dependencies)
- Runs in:
  - Jupyter Notebook
  - Google Colab
  - Any Python IDE (VS Code, PyCharm, etc.)

---

## 📊 Sample Dataset

```python
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}
```
💬 Example Interaction
vbnet
Copy
Edit
👤 You: Which crypto is trending up?
🤖 CryptoBuddy: 📈 These coins are trending up: Bitcoin, Cardano

👤 You: What’s the most sustainable coin?
🤖 CryptoBuddy: 🌱 Cardano is the most sustainable option with minimal energy use!
⚠️ Crypto is risky — always do your own research!

👤 You: Bye
🤖 CryptoBuddy: Catch you later! 💰 Stay smart.
🚀 Getting Started
Clone the repository:
```
bash
git clone https://github.com/Inst3p428/Python-Chat-Bot.git
cd Python-Chat-bot
```
Run the script:

In Terminal:
```
bash
python chatbot.py
```
