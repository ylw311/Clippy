# Clippy

Submitted to HT6 2024

Linda Wang, Edmond Li, Nathan Chung


## Inspiration
Ctrl-C, Ctrl-V: The only two buttons a programmer really needs ;)

We enhance the power of Ctrl-C and Ctrl-V, enabling you to paste seamlessly, leverage AI to analyze your clipboard content, visualize what's on your clipboard, or even play a song!

## What it does
Clippy automatically analyzes your clipboard and provides intelligent suggestions for enhancing, transforming, and utilizing your clipboard content efficiently in your development workflow.

### <u> Matlab AI</u>

Example use cases:

**Play a song**

1. Copy “Play Twinkle Twinkle Little Star”
2. Press Ctrl+v+1 

    This will give you code to play twinkle twinkle little star in Matlab.

    Matlab will automatically run the code it generated to confirm its validity (and so you can enjoy your twinkle twinkle- :)


**Visualize your clipboard content**

1. Copy something like “graph the weather for past 2 months”
2. Press Ctrl+v+1

    This will open Matlab automatically, and display its respective matlab code.

    Clippy will run the matlab code it generated and show you your clipboard content, visualized.


### <u> Adobe Express Add-on</u>

Example use cases:

**Create QR Code**

1. Copy a link (Clippy will also suggest this option if you copied a link)
2. Press Ctrl+v+2

    This will allow you to insert a QR code in Adobe Express, from there you may export and use at your discretion.

### <u>LLM Integration</u>

Example use cases:

**Summarization**

1. Copy a paragraph
2. Press Ctrl+v+3
    
    This will create a summary of your clipboard content.


**Question and Answer**

1. Copy a question like “What are the top ten biggest tech companies in revenue”?”
2. Press Ctrl+v+3
    
    Clippy will answer the question from your clipboard content.


## How we built it

**Langchain**: LLM Engine Development

**FastAPI**: backend server that communicates with Adobe Express, Langchain LLM Engine, and MatLab. 

**OpenAI gpt-4o Model**: LLM for AI generative and instructional tasks 


**Auth0**: OAuth authentication provider

**Sauce Labs**: Testing various components of our application

**Adobe Express**: Interaction with clipboard content

**Matlab**: Visualizing clipboard content

**MongoDB**: Vector Database

## Challenges we ran into
**When a program deletes itself…**

When we tested shortcut “ctrl+v+1”, we didn’t wish to paste the content when we're triggering a feature. To overcome default pasting from "ctrl+v" keybinding, we simulated “ctrl-z” on the system; however, it undid every second “ctrl-v” was pressed - as a result, testing the application caused it to delete itself ;-; 

The running joke goes: “Did we make a malware-” 





## Accomplishments that we're proud of
- Started on Saturday afternoon and finished
- Everyone worked on a piece they weren’t familiar with, the usual “backend peeps” did frontend this time, and vice versa - was a good learning experience for all
- Slept
- Had fun!

## What's next for Clippy

- More Adobe Express features!
- Streamline deployment process for easy setup of all users





## Setup notes


Please take below with a grain of salt, as we were working on multiple features and the setup may not be as straightforward as we'd like.


1. set up your env file with .env.example


2. For Adobe Express:

```zsh
cd qr_code
npm install
npm run build
```
---

Steps:
1. Start adobe express server
2. Open FastAPI server  
3. Run the main.py file

```zsh
uvicorn server:app --reload

cd qr_code
npm run start

python main.py
```

---


uvicorn run on http://127.0.0.1:8000 


Adobe Express default run on https://localhost:5241
