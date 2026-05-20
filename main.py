from core.agent.agent import Agent

agent = Agent()

print("\nHermes Core Başlatıldı")
print("Çıkmak için: exit\n")

while True:

    user_input = input("Sen > ")

    if user_input.lower() == "exit":
        break

    response = agent.run(user_input)

    print(f"\nAgent > {response}\n")