# Maroon6.AI
This project is a simple chatbot that simulates conversations of playable characters in my personal Icewind Dale DnD campaign. It uses the OpenAI GPT-3 language model to generate responses for the characters based on the user's input, which is the situation or dialogue the selected character is engaged in.

The application is fairly simple, leveraging ChatGPT via the OpenAI API and setting characterstics and traits for a character as a 'role'. This then allows you to select a role at the start of the input which generates a different output based on the character selected.

Primarily, this project was created as a small project for me to start experimenting with the OpenAI API via Python and learn about how the API works while building a fun little program to show my friends.

A very basic web interface is included using Flask, though the application performs better via the CLI as the response is noticebly faster via the CLI.

## Pre-requisites
Sign up for an OpenAI API key.
In the python files, replace the openai.api_key value with your API key.
Use pip to install the flask and openai modules

## Usage - Web App version

Start the Flask server by running the following command in your terminal:

    python appversion.py

Open your web browser and go to http://localhost:5000/

Select the character you want to generate content for.

Type your message in the input box and hit Enter/Return or click the "Send" button.

ChatGPT will generate a response based on your input and display it in the chat history.

Continue the conversation by entering additional messages in the input box.

## Usage - Commandline version

Run the commandline version with the following command in your terminal:

    python commandlineversion.py

Select your character by inputting the equivalent number.

Type your message in the input box and hit Enter

ChatGPT will generate a response based on your input and display it in the chat history.

Continue the conversation by entering additional messages in the input box.
