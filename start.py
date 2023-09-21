from engine.core import start

## start running the app
bot = start()

while True:
    response = bot.ask(input("Ask your question: "))
    
    print(response["answer"])
    if response["category"] == "exit":
        break
