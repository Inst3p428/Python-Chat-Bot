# CryptoBuddy Personality
def greet():
    print("👋 Hey there! I’m CryptoBuddy — your friendly crypto guide 🚀")
    print("Ask me about profitable or sustainable cryptocurrencies!")

# Sample Crypto Database
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

def get_most_sustainable():
    return max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])

def get_most_profitable():
    candidates = [coin for coin in crypto_db 
                  if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] == "high"]
    if candidates:
        return candidates[0]
    return "None"

def get_trending_up():
    return [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]

def chatbot():
    greet()
    disclaimer = "⚠️ Crypto is risky — always do your own research!"
    
    while True:
        user_query = input("\nYou: ").lower()
        
        if "exit" in user_query or "bye" in user_query:
            print("CryptoBuddy: Catch you later! 💰 Stay smart.")
            break
        
        elif "sustainable" in user_query:
            coin = get_most_sustainable()
            print(f"CryptoBuddy: 🌱 {coin} is the most sustainable option with minimal energy use!")
            print(disclaimer)
        
        elif "trending" in user_query or "rising" in user_query:
            coins = get_trending_up()
            print(f"CryptoBuddy: 📈 These coins are trending up: {', '.join(coins)}")
            print(disclaimer)

        elif "profitable" in user_query or "best to invest" in user_query or "long-term" in user_query:
            coin = get_most_profitable()
            if coin != "None":
                print(f"CryptoBuddy: 💸 For long-term growth, {coin} looks profitable with a rising trend and high market cap!")
            else:
                print("CryptoBuddy: Hmm, no highly profitable coins found at the moment.")
            print(disclaimer)
        
        elif "info" in user_query or "details" in user_query:
            for name, stats in crypto_db.items():
                print(f"\n{name}:")
                for key, value in stats.items():
                    print(f"  {key}: {value}")
        
        else:
            print("CryptoBuddy: 🤖 Sorry, I didn’t get that. Try asking about trends, sustainability, or investment advice.")


chatbot()
