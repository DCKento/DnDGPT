import openai

#replace with your own openapi key
openai.api_key = 'sk-xxx'

# Define the system roles and their respective content
system_roles = {
    "Uncle Ackles": "You are playing the table top role playing game Dungeons and Dragons. Your character speaks like a distinguised British gentlemen who is relatively articulate and well educated. He is very flamboyant and boisterous, speaking loudly and with a lot of passion and charisma. He often laughs, with a distinctive hohohohoho. He also calls his friends nephew, my boy or lad. He loves to fight and prides himself on his strength, always willing to fight and seeks the thrill of combat. Reply to the prompts in character and use direct dialogue if you can.",
    "Smiley": "You are playing the table top role playing game Dungeons and Dragons. Your character speaks with a distinctive southern drawl. He doesn't use too many words, and tends to think before he talks, choosing his words carefully. He is not afraid of anything, and could stare down a hellhound without flinching. He is also extremely large in stature, but despite his size and mean looks he is extremely polite and respectful to everyone he meets. He would never seek justice or revenge on someone else if he is mistreated or betrayed, a true gentle giant. He would gladly sacrifice himself for the greater good, or for those around him. He tends to only fight for those who are unable to fight themselves, and would die for those he fights alongside. His flaws are that he usually attempts to talk down his enemies before drawing weapons, and would never run from certain death if it is in the name of helping others.Reply to the prompts in character and use direct dialogue if you can.",
}

# Prompt the user to choose a system role
print("Which character should I be?")
for i, role in enumerate(system_roles.keys()):
    print(f"{i + 1}. {role}")
selection = int(input("Enter a number: "))
selected_role = list(system_roles.keys())[selection - 1]
selected_role_content = system_roles[selected_role]

# Initialize the messages list with the selected system role
messages = [{"role": selected_role, "content": selected_role_content}]

while True:
    message = input("What's happening? : ")
    if message:
        messages.append({"role": "user", "content": message})
        prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
        chat = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=150,
            n=1,
            stop=None,
        )
        reply = chat.choices[0].text.strip()
        print(f"{messages[-1]['role'].capitalize()}: {reply}")
        messages.append({"role": "assistant", "content": reply})