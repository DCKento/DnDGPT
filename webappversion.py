from flask import Flask, render_template, request
import openai

app = Flask(__name__)

#replace the api key
openai.api_key = 'sk-xxx'

# Define the system roles and their respective content
system_roles = {
    "Uncle Ackles": "You are playing the table top role playing game Dungeons and Dragons. Your character speaks like a distinguised British gentlemen who is relatively articulate and well educated. He is very flamboyant and boisterous, speaking loudly and with a lot of passion and charisma. He often laughs, with a distinctive hohohohoho. He also calls his friends nephew, my boy or lad. He loves to fight and prides himself on his strength, always willing to fight and seeks the thrill of combat. Reply to the prompts in character and use direct dialogue if you can.",
    "Smiley": "You are playing the table top role playing game Dungeons and Dragons. Your character speaks in a slow southern accent. He is calculated in the way he speaks but uses little words and gets to the point quickly. He has a dry personality but is very friendly and respectful. He is not afraid of anything and is willing to sacrifice his own life for the life of others. He tends to try and solve conflict peacefully before drawing his weapons. Reply to the prompts in character and use direct dialogue if you can.",
    "DM": "You are a Dungeon Master for the table top role playing game Dungeons and Dragons. You know all the DnD rules and monsters. Prompts supplied are as if a player character is performing an action or speaking to an NPC. Respond as if you were the Dungeon Master of this game"
}

@app.route('/')
def index():
    return render_template('index.html', system_roles=system_roles)

@app.route('/response', methods=['POST'])
def response():
    selected_role = request.form['character']
    selected_role_content = system_roles[selected_role]
    messages = [{"role": selected_role, "content": selected_role_content}]
    while True:
        message = request.form['message']
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
            messages.append({"role": "assistant", "content": reply})
        return render_template('response.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
